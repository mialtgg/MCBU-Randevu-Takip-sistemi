from django.db.models import Count
from collections import Counter
from datetime import date
from operator import countOf
from .models import Customer
from django.http import JsonResponse
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



def rapor_view(request):
    today = date.today()
    customers = Customer.objects.all()
    todayCount= Customer.objects.filter(joining_date=today).count()

    # Template'e gönderilecek verileri hazırla
    context = {
        'customers': customers,
        'todayCount':todayCount,
        'today' :today,
    }
    print("rapor_view")
    

    # Template'i render et ve HTTP response'u döndür
    return render(request, 'randevu/rapor.html',context)

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'
    def get_queryset(self):
        return Customer.objects.select_related('user')

def rektördatatable_view(request):
    customers = Customer.objects.all()
    return render(request, 'rektördatatable.html', {'customers': customers})
  

 
  
def succes_view(request):
    customers = Customer.objects.all()
    
    return render(request, 'succes.html',{'customers': customers})
def chart_view(request):
    today = datetime.today()
    current_month = today.month
    current_year = today.year

    daily_counts = Customer.objects.filter(
        joining_date__month=current_month,
        joining_date__year=current_year
    ).annotate(day=ExtractDay('joining_date')) \
        .values('day') \
        .annotate(count=Count('*')) \
        .order_by('day')
    try:
        
     

        # Aylık müşteri sayısını getir
        monthly_counts = Customer.objects.annotate(month=ExtractMonth('joining_date')) \
            .values('month') \
            .annotate(count=Count('*')) \
            .order_by('month')

        weeks = [f'Hafta {i}' for i in range(1, 53)]# Haftalık müşteri sayısını getir
        weekly_counts = Customer.objects.filter(
            joining_date__month=date.today().month
        ).annotate(
            week=ExtractWeek('joining_date')
        ).values(
            'week'
        ).annotate(
            count=Count('*')
        ).order_by('week')
        # Yıllık müşteri sayısını getir
        yearly_counts = Customer.objects.annotate(year=ExtractYear('joining_date')) \
            .values('year') \
            .annotate(count=Count('*')) \
            .order_by('year')

        # ID'leri terminalde görmek için print kullan
        for entry in monthly_counts:
            print(f"Ay {entry['month']} için Aylık Müşteri Sayısı: {entry['count']}")

        for entry in weekly_counts:
            print(f"Hafta {entry['week']} için Haftalık Müşteri Sayısı: {entry['count']}")
        for entry in yearly_counts:
            print(f"Yıl {entry['year']} için Yıllık Müşteri Sayısı: {entry['count']}")

        # View'e aylık, haftalık ve yıllık müşteri sayıları verisini gönder
        context = {'monthly_counts': monthly_counts, 'weekly_counts': weekly_counts, 'yearly_counts': yearly_counts,"weeks":weeks,'daily_counts': daily_counts}

        # View'e aylık ve haftalık müşteri sayıları verisini gönder
        context = {'monthly_counts': monthly_counts, 'weekly_counts': weekly_counts, 'yearly_counts': yearly_counts,"weeks":weeks,'daily_counts': daily_counts}

        print("chart_view fonksiyonu başarıyla tamamlandı")  # Fonksiyonun tamamlandığını kontrol et
        return render(request, 'randevu/chart.html', context)

    except Exception as e:
        print(f"Hata: {e}")  # Hata mesajını terminalde gör
        return render(request, 'randevu/chart.html')  # Hata olması durumunda hata sayfasına yönlendir
def randevu_view(request):

    today = date.today()
    customers = Customer.objects.all()
    todayCount= Customer.objects.filter(joining_date=today).count()
    
    print("lalala")


    # Template'e gönderilecek verileri hazırla
    context = {
        'customers': customers,
        'todayCount':todayCount,
    }
   
    if request.method == 'POST':
    
        
        customer_name = request.POST.get('customer_name')
        konu = request.POST.get('konu')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        joining_date = request.POST.get('joining_date')
        status = request.POST.get('status')

        # Create a new Customer object
        customer = Customer.objects.create(
            
            customer_name=customer_name,
            konu=konu,
            start_time=start_time,
            end_time=end_time,
            joining_date=joining_date,
            status=status
        )

        # Save the object to the database
        customer.save()
        print("randevu_view")

        # Redirect to a success page or wherever you want
        return render(request, 'randevu/rapor.html',context) 

    return render(request, 'randevu/randevu.html')
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete()
    print("delete_customer")
    return redirect('rapor')

# Diğer fonksiyonlar...







