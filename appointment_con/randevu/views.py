from .models import Customer
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomerForm

def randevu_view(request):
    return render(request, 'randevu/randevu.html')
def rapor_view(request):
    return render(request, 'randevu/rapor.html')
def hata_view(request):
    return render(request, 'hata.html')
def succes_view(request):
    return render(request, 'succes.html')
def chart_view(request):
    return render(request, 'randevu/chart.html')
def customer_list(request):
    all_customers = Customer.objects.all().count()
    first_customer = all_customers.first()
  

# Eğer müşteri varsa, verilerini yazdır
    if first_customer:
       print(f"Customer Name: {first_customer.customer_name}")
    
  
    
   
    
    return render(request, 'randevu/rapor.html', {'customers': customers})
print(Customer.objects.all())





def randevu_view(request):
   
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

        # Redirect to a success page or wherever you want
        return redirect('rapor')  # Change 'success_page' to your actual success page

    return render(request, 'randevu/randevu.html')





