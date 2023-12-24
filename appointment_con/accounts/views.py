from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm ,RegisterForm
from django.contrib import messages
from django.views.generic.edit import FormView


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
    return redirect('login')  # Çıkış işlemi tamamlandıktan sonra yönlendirilecek sayfanın adını değiştirin





