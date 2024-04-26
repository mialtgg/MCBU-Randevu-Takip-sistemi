from django import forms
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control' ,
        'placeholder' :'Kullanıcı Adı'}))
    password=forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' :'Şifre'
        }))
    
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu e-posta adresi zaten kayıtlıdır.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Bu kullanıcı adı zaten kullanılmaktadır.")
        return username
   




        

