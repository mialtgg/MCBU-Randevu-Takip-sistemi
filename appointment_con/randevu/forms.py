from django import forms


class RandevuForm(forms.ModelForm):
    ad_soyad = forms.CharField(widget=forms.TextInput(attrs={
        
        }))
    tarih = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
       }))
    randevu_konusu = forms.CharField(widget=forms.TextInput(attrs={
        }))
    iletisim =forms.CharField(widget=forms.TextInput(attrs={
       }))
    sonuc_ekranı=forms.CharField(widget=forms.TextInput(attrs={
        }))
    saatS=forms.TimeField(widget=forms.TimeInput(attrs={
        }))
    saatF=forms.TimeField(widget=forms.TimeInput(attrs={
        }))
    oncelik=forms.IntegerField(widget=forms.TimeInput(attrs={
        }))
    
    
    


    
        
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     tarih = cleaned_data.get('tarih')
    #     saat = cleaned_data.get('saat')
    #     existing_appointment = Randevu.objects.filter(tarih=tarih, saat=saat).first()
    #     if existing_appointment:
    #         raise forms.ValidationError("Bu saat ve tarihde başka bir randevu zaten mevcut.")

    #     return cleaned_data

        
        
