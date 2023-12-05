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
    

class RegisterForm(UserCreationForm) :
    email = forms.EmailField(required=True)

    username=forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control' ,
        'placeholder' :'Kullanıcı Adı'
        }))

    email =forms.EmailField( widget=forms.EmailInput(attrs={
        'class': 'form-control' ,
        'placeholder' :'Email'
        })) 
    
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control' ,
        'placeholder' :'Şifre'
        }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control' ,
        'placeholder' :'Şifreyi Tekrar Girin'
        }))
    
    class Meta:
        model = User
        fields =['username','email','password1','password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu e-posta adresi zaten kayıtlıdır.")
        return email
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Bu kullanıcı adı zaten kullanılmaktadır111. ")
        return username
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Şifreler eşleşmiyor.")
    
   




        

