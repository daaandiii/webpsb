# psb/models.py


from django.db import models
from django.db.models import F
from datetime import datetime
from django.core.exceptions import ValidationError


# Contoh model untuk Kode Area




class Modem(models.Model):
    tipe_modem = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f"{self.tipe_modem} - {self.serial_number}"
    class Meta:
        verbose_name = "Tipe Modem"
        verbose_name_plural = "Tipe Modem"


class Teknisi(models.Model):
    nama_teknisi = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_teknisi
    class Meta:
        verbose_name = "Nama Teknisi"
        verbose_name_plural = "Nama Teknisi"

    


# psb/models.py

class PemasanganBaru(models.Model):
    nama_pelanggan = models.CharField(max_length=255)
    alamat = models.TextField()
    tanggal_pasang = models.DateField()  # Ini mewakili tanggal pemasangan
    paket_layanan = models.ForeignKey('PaketLayanan', on_delete=models.CASCADE)
    modem = models.ForeignKey(Modem, on_delete=models.SET_NULL, null=True, blank=True)
    serial_number_modem = models.CharField(max_length=100, blank=True, null=True)
    teknisi = models.ManyToManyField(Teknisi)
    keterangan = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Panggil method save() asli
        super().save(*args, **kwargs)

        # Cari target bulanan berdasarkan bulan dan tahun dari tanggal pemasangan
        bulan_tahun_pemasangan = self.tanggal_pasang.strftime('%m-%Y')  # Format MM-YYYY
        try:
            target_bulanan = TargetBulanan.objects.get(bulan=bulan_tahun_pemasangan)
        except TargetBulanan.DoesNotExist:
            target_bulanan = None
        
        # Jika target bulanan ditemukan, update current_income dan jumlah user
        if target_bulanan:
            target_bulanan.current_income += self.paket_layanan.harga_paket
            target_bulanan.jumlah_user += 1
            target_bulanan.save()

    def delete(self, *args, **kwargs):
        # Cari target bulanan berdasarkan bulan dan tahun dari tanggal pemasangan
        bulan_tahun_pemasangan = self.tanggal_pasang.strftime('%m-%Y')
        try:
            target_bulanan = TargetBulanan.objects.get(bulan=bulan_tahun_pemasangan)
        except TargetBulanan.DoesNotExist:
            target_bulanan = None

        # Jika target bulanan ditemukan, kurangi current_income dan jumlah user
        if target_bulanan:
            target_bulanan.current_income -= self.paket_layanan.harga_paket
            target_bulanan.jumlah_user -= 1
            target_bulanan.save()

        # Panggil method delete() asli
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.nama_pelanggan} - {self.tanggal_pasang.strftime('%B %Y')}"  # Menggunakan tanggal_pasang, bukan bulan

    class Meta:
        verbose_name = "Pemasangan Baru"
        verbose_name_plural = "Pemasangan Baru"
        ordering = ['-tanggal_pasang']  # Sort by tanggal_pasang



class PaketLayanan(models.Model):
    nama_paket = models.CharField(max_length=255)
    deskripsi = models.TextField()
    harga_paket = models.IntegerField()

    def __str__(self):
        return self.nama_paket

    class Meta:
        verbose_name = "Paket Layanan"
        verbose_name_plural = "Paket Layanan"





# psb/models.py



class TargetBulanan(models.Model):
    bulan = models.CharField(max_length=7)  # Format MM-YYYY
    target_income = models.IntegerField()
    current_income = models.IntegerField(default=0)
    target_user = models.IntegerField()
    jumlah_user = models.IntegerField(default=0)

    def __str__(self):
        return f"Target {self.bulan}"



    def clean(self):
        # Validasi apakah bulan sesuai format MM-YYYY
        try:
            datetime.strptime(self.bulan, '%m-%Y')  # Validasi format bulan
        except ValueError:
            raise ValidationError("Bulan harus dalam format MM-YYYY.")
        

    @property
    def status_target(self):
        income_status = "lebih" if self.current_income >= self.target_income else "kurang"
        user_status = "lebih" if self.jumlah_user >= self.target_user else "kurang"
        return f"Income {income_status}, User {user_status}"

    @property
    def sisa_income(self):
        if self.current_income >= self.target_income:
            return f"Lebih {self.current_income - self.target_income} IDR"
        else:
            return f"Kurang {self.target_income - self.current_income} IDR"

    @property
    def sisa_user(self):
        if self.jumlah_user >= self.target_user:
            return f"Lebih {self.jumlah_user - self.target_user} user"
        else:
            return f"Kurang {self.target_user - self.jumlah_user} user"

    class Meta:
        verbose_name = "Target Bulanan"
        verbose_name_plural = "Target Bulanan"



class LaporanPemasangan(models.Model):
    paket = models.ForeignKey(PaketLayanan, on_delete=models.CASCADE)
    total_user = models.IntegerField()
    jumlah_pelanggan = models.IntegerField()
    nilai_murni = models.IntegerField()
    konversi = models.FloatField()

    def __str__(self):
        return f"Laporan {self.paket.nama_paket}"

    class Meta:
        verbose_name = "Laporan Pemasangan"
        verbose_name_plural = "Laporan Pemasangan"





class KodeArea(models.Model):
    kode = models.CharField(max_length=10)
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama



# Contoh model untuk Jenis Kendala
class JenisKendala(models.Model):
    nama_kendala = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_kendala

# Update field teknisi to be ManyToManyField
class Maintenance(models.Model):
    nama_pelanggan = models.CharField(max_length=100)
    tanggal = models.DateField()
    kode_area = models.ForeignKey(KodeArea, on_delete=models.CASCADE)
    modem = models.ForeignKey(Modem, on_delete=models.SET_NULL, null=True, blank=True)
    sn_modem = models.CharField(max_length=100)
    teknisi = models.ManyToManyField(Teknisi)  # Change to ManyToManyField
    jenis_kendala = models.ForeignKey(JenisKendala, on_delete=models.CASCADE)
    jenis_perbaikan = models.TextField()
    keterangan_lainnya = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama_pelanggan
