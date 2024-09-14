from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import PemasanganBaru, PaketLayanan, TargetBulanan, Modem, Teknisi
from django.db.models import Count, Sum
from datetime import date
from .forms import PemasanganForm
from django.contrib import messages
from .models import PaketLayanan, Modem, Teknisi
from .forms import MaintenanceForm
from .models import Maintenance
from django.db.models.functions import ExtractWeek
from django.shortcuts import render, redirect
from .forms import MaintenanceForm
from django.contrib import messages
import calendar
from django.db.models import Count
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

from datetime import datetime, timedelta
from django.db.models.functions import ExtractWeek, ExtractYear

# Fungsi untuk mendapatkan rentang minggu dalam bulan berdasarkan tanggal
def get_week_ranges_for_month(year, month):
    first_day_of_month = datetime(year, month, 1)
    last_day_of_month = datetime(year, month, calendar.monthrange(year, month)[1])

    week_ranges = []
    start_of_week = first_day_of_month
    while start_of_week <= last_day_of_month:
        end_of_week = min(start_of_week + timedelta(days=6), last_day_of_month)
        week_ranges.append((start_of_week, end_of_week))
        start_of_week = end_of_week + timedelta(days=1)

    return week_ranges

@login_required
def dashboard(request):
    return render(request, 'psb/dashboard.html')

def user_list(request):
    pass  # Logika untuk mengelola pengguna

def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['name']
        user.email = request.POST['email']

        if request.POST['password']:
            user.set_password(request.POST['password'])
        
        user.save()
        messages.success(request, 'Profil berhasil diubah.')

    return render(request, 'psb/profile.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def maintenance_list(request):
    # Dapatkan bulan, tahun, dan minggu dari parameter URL
    bulan = request.GET.get('bulan', None)
    tahun = request.GET.get('tahun', None)
    minggu = request.GET.get('week', None)

    if not bulan:
        bulan = datetime.now().month
    if not tahun:
        tahun = datetime.now().year

    # Buat daftar bulan dalam format angka ke nama bulan
    months = [(i, calendar.month_name[i]) for i in range(1, 13)]

    # Hitung rentang minggu berdasarkan bulan dan tahun yang dipilih
    weeks = get_week_ranges_for_month(int(tahun), int(bulan))

    # Filter berdasarkan bulan dan tahun
    maintenance_data = Maintenance.objects.filter(tanggal__month=bulan, tanggal__year=tahun).order_by('-tanggal')
    
    if minggu:
        # Filter berdasarkan minggu yang dipilih
        selected_week = int(minggu) - 1  # index minggu ke-1 adalah 0
        if selected_week < len(weeks):  # Pastikan minggu berada dalam rentang
            start_of_week, end_of_week = weeks[selected_week]
            maintenance_data = maintenance_data.filter(tanggal__range=[start_of_week, end_of_week]).order_by('-tanggal')


    
    # Grouping data berdasarkan kode area, modem, dan jenis kendala
    kode_area_summary = maintenance_data.values('kode_area__nama').annotate(total=Count('kode_area')).order_by('-total')
    modem_summary = maintenance_data.values('modem__tipe_modem').annotate(total=Count('modem')).order_by('-total')
    kendala_summary = maintenance_data.values('jenis_kendala__nama_kendala').annotate(total=Count('jenis_kendala')).order_by('-total')

    context = {
        'maintenance_data': maintenance_data,
        'kode_area_summary': kode_area_summary,
        'modem_summary': modem_summary,
        'kendala_summary': kendala_summary,
        'selected_bulan': int(bulan),
        'selected_tahun': int(tahun),
        'selected_minggu': int(minggu) if minggu else None,
        'months': months,
        'years': Maintenance.objects.dates('tanggal', 'year', order='DESC'),
        'weeks': list(range(1, len(weeks) + 1)),  # Minggu ke-1 hingga ke-n (dalam bulan)
    }

    return render(request, 'psb/maintenance_list.html', context)




@login_required
def tambah_maintenance(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Maintenance berhasil ditambahkan!')
            
    else:
        form = MaintenanceForm()

    return render(request, 'psb/tambah_maintenance.html', {'form': form})











@login_required
def tambah_pemasangan(request):
    if request.method == 'POST':
        form = PemasanganForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pemasangan berhasil ditambahkan!')  # Add success message
            return redirect('psb')  # Redirect to the PSB page after saving
    else:
        form = PemasanganForm()

    # Get the list of available options for paket, modem, and teknisi
    paket_list = PaketLayanan.objects.all()
    modem_list = Modem.objects.all()
    teknisi_list = Teknisi.objects.all()

    return render(request, 'psb/psb.html', {
        'form': form,
        'paket_list': paket_list,
        'modem_list': modem_list,
        'teknisi_list': teknisi_list,
    })









@login_required
def psb_view(request):
    return render(request, 'psb/psb.html')


@login_required
def pemasangan_list(request):
    # Default bulan dan tahun
    bulan = request.GET.get('bulan') or str(date.today().month)
    tahun = request.GET.get('tahun') or str(date.today().year)

    pemasangan_list = PemasanganBaru.objects.all()

    # Filter berdasarkan bulan dan tahun
    if bulan and tahun:
        pemasangan_list = pemasangan_list.filter(tanggal_pasang__year=tahun, tanggal_pasang__month=bulan)

    # Dapatkan target bulanan berdasarkan bulan dan tahun yang dipilih
    bulan_tahun = f"{int(bulan):02d}-{tahun}"
    target_bulanan = TargetBulanan.objects.filter(bulan=bulan_tahun).first()

    # Hitung total user dan income dari pemasangan
    total_user_all = pemasangan_list.count()
    total_income_all = pemasangan_list.aggregate(Sum('paket_layanan__harga_paket'))['paket_layanan__harga_paket__sum'] or 0

    # Sisa user dan sisa income (bilangan positif jika sudah lebih)
    if target_bulanan:
        target_user = target_bulanan.target_user  # target user bulanan
        sisa_income = total_income_all - target_bulanan.target_income
        sisa_user = total_user_all - target_user
        
        # Pastikan bilangan positif untuk kelebihan
        sisa_income_abs = abs(sisa_income) if sisa_income < 0 else sisa_income
        sisa_user_abs = abs(sisa_user) if sisa_user < 0 else sisa_user
    else:
        target_user = 0
        sisa_income = 0
        sisa_user = 0
        sisa_income_abs = 0
        sisa_user_abs = 0

    # Hitung konversi dan jumlah user untuk setiap paket layanan
    paket_data = pemasangan_list.values(
        'paket_layanan__nama_paket', 'paket_layanan__harga_paket'
    ).annotate(
        total_user=Count('paket_layanan'),
        total_income=Sum('paket_layanan__harga_paket')
    )

    # Hitung konversi setiap paket
    for paket in paket_data:
        paket['konversi'] = (paket['total_user'] / total_user_all) * 100 if total_user_all > 0 else 0

    # Dapatkan daftar teknisi dan modem
    teknisi_data = Teknisi.objects.all()
    modem_data = Modem.objects.all()

    # Kirim data ke template
    years = range(2020, date.today().year + 1)

    return render(request, 'psb/pemasangan_list.html', {
        'pemasangan_list': pemasangan_list,
        'paket_data': paket_data,
        'total_user_all': total_user_all,  # Jumlah total user (user saat ini)
        'total_income_all': total_income_all,
        'target_bulanan': target_bulanan,
        'target_user': target_user,
        'sisa_income': sisa_income,
        'sisa_income_abs': sisa_income_abs,
        'sisa_user': sisa_user,
        'sisa_user_abs': sisa_user_abs,
        'years': years,  # Daftar tahun untuk dropdown
        'selected_bulan': int(bulan),  # Bulan yang dipilih oleh user
        'selected_tahun': int(tahun),  # Tahun yang dipilih oleh user
        'modem_data': modem_data,  # Data modem untuk ditampilkan
        'teknisi_data': teknisi_data,  # Data teknisi untuk ditampilkan
    })

