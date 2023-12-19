from django.db.models import Count
from collections import Counter
from datetime import date
from operator import countOf
from .models import Customer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomerForm
from django.db.models.functions import ExtractMonth
from django.shortcuts import render
from .models import Customer

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
def hata_view(request):
    return render(request, 'hata.html')
def succes_view(request):
    return render(request, 'succes.html')
def chart_view(request):
    return render(request, 'randevu/chart.html')
def randevu_view(request):

    today = date.today()
    customers = Customer.objects.all()
    todayCount= Customer.objects.filter(joining_date=today).count()
    



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

def get_customer_ids_and_names(request):
    
    # Veritabanındaki tüm müşterilerin id ve customer_name alanlarını getir
    customers = Customer.objects.values('id', 'customer_name')
    
    for customer in customers:
        print(f"Customer Name: {Customer.customer_name} - ID: {customer.id}")

    # View'e müşteri bilgilerini gönder
    context = {'customers': customers}
    print("get_customer_ids_and_names")
    return render(request, 'chart.html', context)

def monthly_customer_count(request):
    # Müşteri sayısını aylık olarak geti
    print("2")
    
    
    monthly_counts = Customer.objects.annotate(month=ExtractMonth('joining_date')) \
        .values('month') \
        .annotate(count=Count('id')) \
        .order_by('month')

    # View'e aylık müşteri sayıları verisini gönder
    context = {'monthly_counts': monthly_counts}
    customers = Customer.objects.all()

    # ID'leri terminalde görmek için print kullan
    for entry in monthly_counts:
        print(f"Ay {entry['month']} için Müşteri ID'leri: {entry['id']}")
        print("monthly_count")

    return render(request, 'chart.html', context)





