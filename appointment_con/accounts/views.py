from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm ,RegisterForm
from django.contrib import messages
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ChangePasswordForm

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ChangePasswordForm

from crispy_forms.layout import Layout, Submit, Field, Div

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def user_login(request):
    print('1')
    print(request.method)
    if request.method == "POST":
        print('2')
        form = LoginForm(request.POST)
        print("hereee")
        print(form,"wssds")
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print('3')
            if user is not None and user.is_active:
                login(request, user)
                return redirect('succes')
            else:
                messages.error(request, 'Geçersiz Şifre ya da Kullanıcı adı')
        else:
            messages.error(request, 'Böyle Bir kullanıcı Yok')
    else:
        print('5')
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})
               
@csrf_exempt              
def user_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kayıt başarılı. Şimdi giriş yapabilirsiniz.')
            return redirect('login')
        else:
            messages.error(request, 'Kayıt başarısız. Lütfen aşağıdaki hataları düzeltin.')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form})

    
def logout_view(request):
    logout(request)
    return redirect('login') 



from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ChangePasswordForm

@login_required
def password_change(request):
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = request.user
            old_password = form.cleaned_data['old_password']
            new_password1 = form.cleaned_data['new_password1']
            new_password2 = form.cleaned_data['new_password2']
            if user.check_password(old_password):
                if new_password1 == new_password2:
                    user.set_password(new_password1)
                    user.save()
                    update_session_auth_hash(request, user)
                    
                    return render(request, 'succes.html', {'form': form})
                else:
                    messages.error(request, 'Yeni şifreler uyuşmuyor.')
            else:
                messages.error(request, 'Eski şifreniz doğru değil.')
                
    else:
        form = ChangePasswordForm()
        
        form.helper = None

    # Crispy Forms kullanarak form alanlarını biçimlendir
    form.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Eski Şifreniz'})
    form.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Yeni Şifreniz'})
    form.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Yeni Şifrenizi Tekrar Girin'})

    return render(request, 'password_change.html', {'form': form})
    
