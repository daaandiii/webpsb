# Generated by Django 5.1.1 on 2024-09-11 04:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psb', '0012_alter_targetbulanan_bulan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipe_modem', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teknisi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_teknisi', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='pemasanganbaru',
            name='serial_number_modem',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pemasanganbaru',
            name='modem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='psb.modem'),
        ),
        migrations.AddField(
            model_name='pemasanganbaru',
            name='teknisi',
            field=models.ManyToManyField(to='psb.teknisi'),
        ),
    ]
