
#class PemasanganBaruForm(forms.ModelForm):
#    class Meta:
#        model = PemasanganBaru
#        fields = '__all__'
#        widgets = {
#            'teknisi': forms.CheckboxSelectMultiple,
#        }




from django import forms
from .models import PemasanganBaru, Maintenance, PaketLayanan, Modem, Teknisi




class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = '__all__'
        widgets = {
            'teknisi': forms.CheckboxSelectMultiple(),  # Menggunakan checkbox untuk multiple choice teknisi
            'tanggal': forms.DateInput(attrs={'type': 'date'}),  # Menambahkan date picker untuk tanggal
            'kode_area': forms.Select(attrs={'class': 'form-select'}),  # Dropdown dengan Bootstrap style
            'modem': forms.Select(attrs={'class': 'form-select'}),  # Dropdown untuk Modem
            'jenis_kendala': forms.Select(attrs={'class': 'form-select'}),  # Dropdown untuk Jenis Kendala
            'sn_modem': forms.TextInput(attrs={'class': 'form-control'}),  # Input untuk SN Modem
            'jenis_perbaikan': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),  # Textarea untuk jenis perbaikan
            'keterangan_lainnya': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Opsional'}),  # Textarea untuk keterangan lain
        }

    def __init__(self, *args, **kwargs):
        super(MaintenanceForm, self).__init__(*args, **kwargs)
        self.fields['nama_pelanggan'].widget.attrs.update({'class': 'form-control'})  # Menambahkan class ke nama_pelanggan
        self.fields['teknisi'].queryset = Teknisi.objects.all()  # Menampilkan semua teknisi yang ada di database





class PemasanganForm(forms.ModelForm):
    # Paket Layanan selection
    paket_layanan = forms.ModelChoiceField(
        queryset=PaketLayanan.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    # Modem selection
    modem = forms.ModelChoiceField(
        queryset=Modem.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    # Teknisi selection with multiple choice
    teknisi = forms.ModelMultipleChoiceField(
        queryset=Teknisi.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    
    class Meta:
        model = PemasanganBaru
        fields = '__all__'  # Include all fields in the form
        widgets = {
            'tanggal_pasang': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nama_pelanggan': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control'}),
            'serial_number_modem': forms.TextInput(attrs={'class': 'form-control'}),
            'keterangan': forms.Textarea(attrs={'class': 'form-control'}),
        }


#class PemasanganForm(forms.ModelForm):
#    paket_layanan = forms.ModelChoiceField(
#        queryset=PaketLayanan.objects.all(),
#        widget=forms.Select(attrs={'class': 'form-control'})
#    )
#    modem = forms.ModelChoiceField(
#        queryset=Modem.objects.all(),
#        widget=forms.Select(attrs={'class': 'form-control'})
#    )
#    teknisi = forms.ModelMultipleChoiceField(
#        queryset=Teknisi.objects.all(),
#        widget=forms.CheckboxSelectMultiple
#    )
    
#    class Meta:
#        model = PemasanganBaru
#        fields = ['nama_pelanggan', 'alamat', 'tanggal_pasang', 'paket_layanan', 'modem', 'serial_number_modem', 'teknisi', 'keterangan']
#        widgets = {
#            'tanggal_pasang': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
 #           'nama_pelanggan': forms.TextInput(attrs={'class': 'form-control'}),
  #          'alamat': forms.Textarea(attrs={'class': 'form-control'}),
   #         'serial_number_modem': forms.TextInput(attrs={'class': 'form-control'}),
   #         'keterangan': forms.Textarea(attrs={'class': 'form-control'}),
    #    }
