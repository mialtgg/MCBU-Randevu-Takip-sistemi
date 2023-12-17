from .models import Customer
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomerForm

def randevu_view(request):
    return render(request, 'randevu/randevu.html')
def rapor_view(request):
    return render(request, 'randevu/rapor.html')

def randevu_view(request):
    if request.method == 'POST':
        # Get data from the form
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
        return redirect('success_page')  # Change 'success_page' to your actual success page

    # Render the form template for GET requests
    return render(request, 'randevu/randevu.html')