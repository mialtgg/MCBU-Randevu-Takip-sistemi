from django.db.models import Count
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta, timezone
from django.contrib import messages
from django.forms import ValidationError

from .models import Customer
from django.http import HttpResponseServerError, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomerForm
from django.db.models.functions import ExtractMonth, ExtractWeek, ExtractYear,ExtractDay
from django.shortcuts import render
from django.shortcuts import render
from .models import Customer
from datetime import datetime
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q



def rapor_view(request):
    if request.user.is_authenticated:
     user_id = request.user.id
     username= request.user.username
    today = date.today()

    if(username == "mustakılban"):
        customers = Customer.objects.filter(Q(user_id=user_id) & Q(admin_add_name="user1"))
    elif(username == "pelinkosan"):
        customers = Customer.objects.filter(Q(user_id=user_id) |  Q(admin_add_name="user3"))
    elif(username == "aysunokumus"):
        customers = Customer.objects.filter(Q(user_id=user_id) &  Q(admin_add_name="user4"))
    elif(username == "nurdagulerturk"):
        customers = Customer.objects.filter(Q(user_id=user_id) |  Q(admin_add_name="user2"))
    elif(username == "baharkocer"):
        customers = Customer.objects.filter(Q(user_id=user_id) |  Q(admin_add_name="user5"))
    else:
        customers = Customer.objects.all()



    todayCount = customers.filter(joining_date=date.today()).count()
    # Template'e gönderilecek verileri hazırla
    context = {
        'customers': customers,
        'todayCount':todayCount,
        'today' :today,
    }
    
    

    # Template'i render et ve HTTP response'u döndür
    return render(request, 'randevu/rapor.html',context)





class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'
    def get_queryset(self):
        return Customer.objects.select_related('user')
    

def is_admin(user):
    return user.is_authenticated and user.is_staff
    
@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def rektördatatable_view(request):
    customers = Customer.objects.all()

    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            user_id = request.user.id
            customer_name = form.cleaned_data['customer_name']
            konu = form.cleaned_data['konu']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            joining_date = form.cleaned_data['joining_date']
            status = form.cleaned_data['status']
            admin_add_name = form.cleaned_data['admin_add_name']

            existing_customers = customers.filter(
                start_time__gte=start_time,
                end_time__lte=end_time,
                joining_date=joining_date,
                admin_add_name__in=["user1", "user2", "user3", "user4","user5"]
                
            )

            if existing_customers.exists():
                messages.error(request, "Bu saat aralığında aynı tarihe başka bir randevunuz var, ekleme yapılmadı")
            else:
                customer = Customer.objects.create(
                    user_id=user_id,
                    customer_name=customer_name,
                    konu=konu,
                    start_time=start_time,
                    end_time=end_time,
                    joining_date=joining_date,
                    status=status,
                    admin_add_name=admin_add_name
                )

                customer.save()
                messages.success(request, "Randevu başarıyla oluşturuldu.")
                
            return render(request, 'rektördatatable.html', {'customers': customers, 'form': form})
        else:
            messages.error(request, "Form geçersiz, lütfen tüm gerekli alanları doldurun.")
            return render(request, 'rektördatatable.html', {'customers': customers, 'form': form})
    else:
        form = CustomerForm()
        return render(request, 'rektördatatable.html', {'customers': customers, 'form': form})

@login_required
def succes_view(request):
    user_id = request.user.id
    today = date.today()
    customers_today = Customer.objects.filter(user_id=user_id, joining_date__gte=today).values('customer_name', 'joining_date', 'start_time')[:10]

    context = {'customers_today': customers_today}
    print(customers_today)
    return render(request, 'succes.html', context)




@login_required
def chart_view(request):
    user_id = request.user.id

    today = datetime.today()
    current_month = today.month
    current_year = today.year

    daily_counts = Customer.objects.filter(
        user_id=user_id,
        joining_date__month=current_month,
        joining_date__year=current_year
    ).annotate(day=ExtractDay('joining_date')) \
        .values('day') \
        .annotate(count=Count('*')) \
        .order_by('day')

    try:
        # Aylık müşteri sayısını getir
        monthly_counts = Customer.objects.filter(
            user_id=user_id
        ).annotate(month=ExtractMonth('joining_date')) \
            .values('month') \
            .annotate(count=Count('*')) \
            .order_by('month')
        
        month_names = [
    'Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran',
    'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'
]
        weeks = [f'Hafta {i}' for i in range(1, 53)]

        # Haftalık müşteri sayısını getir
        weekly_counts = Customer.objects.filter(
            user_id=user_id,
            joining_date__month=date.today().month
        ).annotate(
            week=ExtractWeek('joining_date')
        ).values(
            'week'
        ).annotate(
            count=Count('*')
        ).order_by('week')

        # Yıllık müşteri sayısını getir
        yearly_counts = Customer.objects.filter(
            user_id=user_id
        ).annotate(year=ExtractYear('joining_date')) \
            .values('year') \
            .annotate(count=Count('*')) \
            .order_by('year')

        # View'e aylık, haftalık ve yıllık müşteri sayıları verisini gönder
        context = {
            'monthly_counts': monthly_counts,
            'weekly_counts': weekly_counts,
            'yearly_counts': yearly_counts,
            'weeks': weeks,
            'daily_counts': daily_counts,
            'month_names' :month_names
        }

        print("chart_view fonksiyonu başarıyla tamamlandı")
        return render(request, 'randevu/chart.html', context)

    except Exception as e:
        print(f"Hata: {e}")
        return render(request, 'randevu/chart.html')


@login_required
def randevu_view(request):
    # Eğer kullanıcı admin ise veya oturum açmışsa
    if request.user.is_staff or request.user.is_authenticated:
        user_id = request.user.id 
        username= request.user.username

        today = date.today()
        customers = Customer.objects.filter(user_id=user_id )
        todayCount = customers.filter(joining_date=today).count()

        # Template'e gönderilecek verileri hazırla
        context = {
            'customers': customers,
            'todayCount': todayCount,
        }

        if request.method == 'POST':
            customer_name = request.POST.get('customer_name')
            konu = request.POST.get('konu')
            start_time_str = request.POST.get('start_time')
            end_time_str = request.POST.get('end_time')
            joining_date = request.POST.get('joining_date')
            status = request.POST.get('status')
            admin_add_name=request.POST.get('admin_add_name')
            if(username == "mustakılban"):
                admin_add_name="user1"
            elif(username =="pelinkosan"):
                admin_add_name="user3"
            elif(username =="nurdagulerturk"):
                admin_add_name="user2"
            elif(username =="baharkocer"):
                admin_add_name="user5"
            elif(username  =="aysunokumus"):
                admin_add_name="user4"


            # datetime nesnelerini oluştur
            start_time = datetime.strptime(start_time_str, '%H:%M')
            end_time = datetime.strptime(end_time_str, '%H:%M')
            

            existing_customers = customers.filter(
                start_time__gte=start_time,
                start_time__lte=end_time,
                joining_date=joining_date,
                
            )
            
            if existing_customers.exists():
                messages.error(request, "Bu saat aralığında aynı tarihe başka bir randevunuz var, ekleme yapılmadı")
            else:
                # Create a new Customer object
                customer = Customer.objects.create(
                    user_id=user_id,
                    customer_name=customer_name,
                    konu=konu,
                    start_time=start_time,
                    end_time=end_time,
                    joining_date=joining_date,
                    status=status,
                    admin_add_name=admin_add_name
                )

                # Save the object to the database
                customer.save()

                messages.success(request, "Randevu başarıyla oluşturuldu.")

        return render(request, 'randevu/randevu.html', context)
    else:
        return redirect('login')  # Kullanıcı oturum açmamışsa, login sayfasına yönlendir
def delete_customer(request, customer_id):
    print(request)
    try:
        customer = get_object_or_404(Customer, id=customer_id)
        print(customer)
        customer.delete()
        print("hola")
        return redirect(rapor_view)
    except Customer.DoesNotExist as e:
        print("1")
        print(f"Customer not found: {e}")
        return HttpResponseServerError("Customer not found.")
    except Exception as e:
        print("23")
        # Diğer olası hata durumları için özel işlemler ekleyebilirsiniz.
        print(f"An error occurred: {e}")
        return HttpResponseServerError(f"An error occurred: {e}")

def edit_customer(request, customer_id):
    # URL'den gelen customer_id parametresi ile müşteri objesini al
    customer = get_object_or_404(Customer, id=customer_id)
   
    print("1")

    if request.method == 'POST':
        print("2")
        # Eğer HTTP isteği bir POST isteği ise, formdan gelen verileri al
        customer_name = request.POST.get('customer_name')
        konu = request.POST.get('konu')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        joining_date = request.POST.get('joining_date')
        status = request.POST.get('status')

        # Varolan müşteri objesini güncelle
        customer.customer_name = customer_name
        customer.konu = konu
        customer.start_time = start_time
        customer.end_time = end_time
        customer.joining_date = joining_date
        customer.status = status

        # Güncellenmiş müşteriyi veritabanına kaydet
        customer.save()
        return redirect(rapor_view)

    else:
        print("3")
        # Eğer istek bir POST isteği değilse, formu müşteri verileriyle doldur
        form = CustomerForm(instance=customer)
        return redirect(rapor_view)

    # Müşteri objesini ve formu şablonla birlikte render et
    