# Generated by Django 5.1.1 on 2024-09-11 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psb', '0013_modem_teknisi_pemasanganbaru_serial_number_modem_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modem',
            options={'verbose_name': 'Tipe Modem', 'verbose_name_plural': 'Tipe Modem'},
        ),
        migrations.AlterModelOptions(
            name='teknisi',
            options={'verbose_name': 'Nama Teknisi', 'verbose_name_plural': 'Nama Teknisi'},
        ),
    ]
