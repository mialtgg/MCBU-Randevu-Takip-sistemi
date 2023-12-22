from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm ,RegisterForm
from django.contrib import messages
from django.views.generic.edit import FormView

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def user_login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,
                                password = password)
            

            if user is not None: #böyle bir kullanıcı varsa
                if user.is_active:
                   
                    login(request,user)
                    return redirect('succes')
                    
                else:
                    messages.info(request,'Disabled Account')
                    
            else:
               
               messages.info(request,'Email Ya da şifre Yanlış')
               
        else:
         
            messages.info(request,'Disabled Account')
          
    else:
       
        form = LoginForm()

    return render(request,'account/login.html',{'form':form})
               
               
def user_register(request):
    
    if request.method == "POST":
        print("1")
        form = RegisterForm(request.POST)
        if form.is_valid():
            
            print("2")
            form.save()
            messages.success(request,form.errors)
            return redirect ('login')
        else:
           print(form.errors)
           messages.error(request,form.errors)
    else :
        form=RegisterForm()
    return render(request,'account/register.html',{'form':form})   
    
def logout_view(request):
    logout(request)
    return redirect('login')  # Çıkış işlemi tamamlandıktan sonra yönlendirilecek sayfanın adını değiştirin





