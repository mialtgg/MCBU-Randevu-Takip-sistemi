from django.db.models import Count
from django.contrib.auth.decorators import login_required
from datetime import date, timezone
from django.contrib import messages
from django.utils import timezone
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
from django.http import HttpResponse
from excel_response import ExcelResponse
from django.shortcuts import render
from openpyxl import Workbook
from django.http import HttpResponse

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

    

    
    customers = customers.filter(deleted=False)
    



    todayCount = customers.filter(joining_date=date.today()).count()
    # Template'e gönderilecek verileri hazırla
    context = {
        'customers': customers,
        'todayCount':todayCount,
        'today' :today,
    }
    
    

    # Template'i render et ve HTTP response'u döndür
    return render(request, 'randevu/rapor.html',context)
def is_admin(user):
    return user.is_authenticated and user.is_staff
    
@user_passes_test(lambda u: u.is_staff, login_url='/login/')

def rektördatatable_view(request):
    try:
        customers = Customer.objects.filter(deleted=False)

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

                # Aynı saat aralığı ve tarih için müşteri kontrolü
                existing_customers = customers.filter(
                    start_time__gte=start_time,
                    end_time__lte=end_time,
                    joining_date=joining_date,
                    admin_add_name__in=["user1", "user2", "user3", "user4", "user5"]
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
                    messages.success(request, "Randevu başarıyla oluşturuldu")

                # Burada filtreleme yaparak sadece silinmemiş müşterileri alabilirsiniz
                customers = Customer.objects.filter(deleted=False)

                return render(request, 'rektördatatable.html', {'customers': customers, 'form': form})
            else:
                messages.error(request, "Form geçersiz, lütfen tüm gerekli alanları doldurun")
                return render(request, 'rektördatatable.html', {'customers': customers, 'form': form})
        else:
            form = CustomerForm()
            return render(request, 'rektördatatable.html', {'customers': customers, 'form': form})
    except Exception as e:
        return HttpResponseServerError(f"Bir hata oluştu: {e}")


@login_required
def succes_view(request):
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
        
        customers=Customer.objects.filter(deleted=False)

    customers_today = customers.filter(joining_date__gte=today,deleted=False)[:10]
    
  

    context = {'customers_today':customers_today}
    

    return render(request, 'succes.html', context)




@login_required
def chart_view(request):
    user_id = request.user.id
    username= request.user.username
    today = datetime.today()
    admin_add_name = None
    

    if username == "mustakılban":
        admin_add_name = "user1"
    elif username == "pelinkosan":
        admin_add_name = "user3"
    elif username == "aysunokumus":
        admin_add_name = "user4"
    elif username == "nurdagulerturk":
        admin_add_name = "user2"
    elif username == "baharkocer":
        admin_add_name = "user5"

    customers = Customer.objects.filter(user_id=user_id, admin_add_name=admin_add_name, deleted=False)


   
    


    current_month = today.month
    current_year = today.year
    


    daily_counts = Customer.objects.filter(
        user_id=user_id ,
        admin_add_name=admin_add_name,
        joining_date__month=current_month,
        joining_date__year=current_year,
        deleted=False,
       
        
    ).annotate(day=ExtractDay('joining_date')) \
        .values('day') \
        .annotate(count=Count('*')) \
        .order_by('day')

    try:
        # Aylık müşteri sayısını getir
        monthly_counts = Customer.objects.filter(
            user_id=user_id,
            admin_add_name=admin_add_name,
            deleted=False
            
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
            admin_add_name=admin_add_name,
            joining_date__month=date.today().month,
            deleted=False
        ).annotate(
            week=ExtractWeek('joining_date')
        ).values(
            'week'
        ).annotate(
            count=Count('*')
        ).order_by('week')

        # Yıllık müşteri sayısını getir
        yearly_counts = Customer.objects.filter(
            user_id=user_id,
            admin_add_name=admin_add_name,
            deleted=False
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
            'month_names' :month_names,
            'customers': customers,
            

        }

  
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
        if(username=="mustakılban"):
             customers = Customer.objects.filter(Q(user_id=user_id) & Q(admin_add_name="user1"))
        elif(username == "pelinkosan"):
             customers = Customer.objects.filter(Q(user_id=user_id) |  Q(admin_add_name="user3"))
        elif(username == "aysunokumus"):
            customers = Customer.objects.filter(Q(user_id=user_id) &  Q(admin_add_name="user4"))
        elif(username == "nurdagulerturk"):
            customers = Customer.objects.filter(Q(user_id=user_id) |  Q(admin_add_name="user2"))
        elif(username == "baharkocer"):
            customers = Customer.objects.filter(Q(user_id=user_id) |  Q(admin_add_name="user5"))
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

        # Müşteriyi silmek yerine 'deleted' alanını True olarak işaretle
        customer.deleted = True
        customer.deleted_time = timezone.now()
        customer.save()

        return redirect(rapor_view)
    except Customer.DoesNotExist as e:
        return HttpResponseServerError("Müşteri bulunamadı.")
    except Exception as e:
        return HttpResponseServerError(f"Bir hata oluştu: {e}")

def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)

    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        konu = request.POST.get('konu')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        joining_date = request.POST.get('joining_date')
        status = request.POST.get('status')
        customer.customer_name = customer_name
        customer.konu = konu
        customer.start_time = start_time
        customer.end_time = end_time
        customer.joining_date = joining_date
        customer.status = status
        customer.save()  
        return redirect(rapor_view)

    else:
        form = CustomerForm(instance=customer)
        return redirect(rapor_view)

def delated_page_view(request):
    customers=Customer.objects.filter(deleted=True)
    context = {'customer': customers}
   
    context = {
        'customers': customers
    }
 
    return render(request , 'delated_page.html',context)

def edited_page_view(request):
    customers= Customer.objects.filter()

    context = {
        'customers': customers
    }
    

    return render(request, 'edited_page.html', context)

def export_to_excel(request):
     # Sadece silinmemiş randevuları al
    queryset = Customer.objects.filter(deleted=False)

    selected_fields = ['customer_name', 'konu', 'start_time', 'end_time', 'joining_date', 'status', 'admin_add_name']
    filtered_queryset = queryset.values(*selected_fields)

    workbook = Workbook()
    worksheet = workbook.active

    # Başlık satırını ekle
    title_row = ['Talep Eden Kişi', 'Konu', 'Başlama Zamanı', 'Bitiş Zamanı', 'Randevu Tarihi', 'Durumu', 'Randevuyu Oluşturan Kişi']
    worksheet.append(title_row)

      # Verileri ekleyin
    for customer in queryset:
        row = {}
        for field in selected_fields:
            if field == 'status':
                # Burada status'a özel bir dönüşüm yapın
                status_display = {
                    'Active': 'Aktif',
                    'Block': 'İptal Edildi',
                    # Diğer durumlar için gerektiği gibi ekleyin
                }.get(customer.status, customer.status)
                print(status_display)
                row[field] = status_display
            elif field == 'admin_add_name':
                # admin_add_name için özel dönüşüm
                admin_add_name_display = {
                    'user1': 'M.Müştak İLBAN',
                    'user2': 'Nurdagül ERTÜRK',
                    'user3': 'Pelin KOŞAN',
                    'user4': 'Aysun OKUMUŞ',
                    'user5': 'Bahar Koçer',
                }.get(customer.admin_add_name, customer.admin_add_name)

                row[field] = admin_add_name_display
            else:
                row[field] = str(getattr(customer, field))
        worksheet.append([row[field] for field in selected_fields])

        

    # HttpResponse kullanarak dosyayı kullanıcıya geri döndürün
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="radevularım.xlsx"'
    workbook.save(response)

    return response

