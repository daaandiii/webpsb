# psb/admin.py

from django.contrib import admin
from .models import PemasanganBaru, PaketLayanan, LaporanPemasangan, TargetBulanan, Modem, Teknisi
from .models import Maintenance  # Import model Maintenance
from django.contrib import admin
from .models import KodeArea, JenisKendala




class TargetBulananAdmin(admin.ModelAdmin):
    list_display = ('bulan', 'target_income', 'target_user', 'jumlah_user')
    #list_display = ('bulan', 'target_income', 'current_income', 'target_user', 'jumlah_user', 'status_target', 'sisa_income', 'sisa_user')

#@admin.register(PemasanganBaru)
#class PemasanganBaruAdmin(admin.ModelAdmin):
#    list_display = ['nama_pelanggan', 'alamat', 'tanggal_pasang', 'modem', 'serial_number_modem']
#    filter_horizontal = ['teknisi']



class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ['nama_pelanggan', 'tanggal', 'kode_area', 'modem', 'teknisi']
    search_fields = ['nama_pelanggan', 'sn_modem']



# Register your models here.
admin.site.register(Maintenance)  # Daftarkan model Maintenance di admin
admin.site.register(Modem)
admin.site.register(Teknisi)
admin.site.register(PemasanganBaru)
admin.site.register(PaketLayanan)
admin.site.register(LaporanPemasangan)
admin.site.register(TargetBulanan, TargetBulananAdmin)
admin.site.register(KodeArea)
admin.site.register(JenisKendala)


