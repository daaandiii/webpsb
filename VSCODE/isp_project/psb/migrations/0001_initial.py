# Generated by Django 5.1.1 on 2024-09-09 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaketLayanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_paket', models.CharField(max_length=255)),
                ('deskripsi', models.TextField()),
                ('harga_paket', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PemasanganBaru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pelanggan', models.CharField(max_length=255)),
                ('alamat', models.TextField()),
                ('tanggal_pasang', models.DateField()),
                ('nominal', models.IntegerField()),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TargetBulanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bulan', models.CharField(max_length=50)),
                ('target_income', models.IntegerField()),
                ('current_income', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LaporanPemasangan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_user', models.IntegerField()),
                ('jumlah_pelanggan', models.IntegerField()),
                ('nilai_murni', models.IntegerField()),
                ('konversi', models.FloatField()),
                ('paket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psb.paketlayanan')),
            ],
        ),
    ]
