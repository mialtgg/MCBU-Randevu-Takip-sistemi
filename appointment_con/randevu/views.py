# from .models import Customer
# from django.http import JsonResponse
# from django.shortcuts import redirect, render
# from django.views.decorators.csrf import csrf_exempt
# from .forms import CustomerForm

# def randevu_view(request):
#     return render(request, 'randevu/randevu.html')
# def rapor_view(request):
#     return render(request, 'randevu/rapor.html')

# def hata_view(request):
#     return render(request, 'hata.html')
# def succes_view(request):
#     return render(request, 'succes.html')
# def chart_view(request):
#     return render(request, 'randevu/chart.html')





# def randevu_view(request):
   
#     if request.method == 'POST':
    
        
#         customer_name = request.POST.get('customer_name')
#         konu = request.POST.get('konu')
#         start_time = request.POST.get('start_time')
#         end_time = request.POST.get('end_time')
#         joining_date = request.POST.get('joining_date')
#         status = request.POST.get('status')

#         # Create a new Customer object
#         customer = Customer.objects.create(
            
#             customer_name=customer_name,
#             konu=konu,
#             start_time=start_time,
#             end_time=end_time,
#             joining_date=joining_date,
#             status=status
#         )

#         # Save the object to the database
#         customer.save()

#         # Redirect to a success page or wherever you want
#         return redirect('rapor')  # Change 'success_page' to your actual success page

#     return render(request, 'randevu/randevu.html')
from .models import Item
from collections import Counter
from datetime import date
from .models import Customer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomerForm
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('rapor')


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
    print(todayCount)



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
        

        # Redirect to a success page or wherever you want
        return render(request, 'randevu/rapor.html',context) 

    return render(request, 'randevu/randevu.html')





