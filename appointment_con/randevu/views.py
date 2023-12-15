from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import EventForm


def randevu_view(request):
    return render(request, 'randevu/randevu.html')
def rapor_view(request):
    return render(request, 'randevu/rapor.html')
@csrf_exempt
def save_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        print("2")
        
        if form.is_valid():
            
            print("1")
            event = form.save()
            cleaned_data = form.cleaned_data
            print("forma save edildikten sonra:", cleaned_data)
            return JsonResponse({'status': 'success', 'message': 'Etkinlik başarıyla kaydedildi'})
        else:
            print("3")
            errors = form.errors.as_json()
            
            # Hataları terminalde yazdır
            print("Form Hataları:", errors)
            
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        return JsonResponse({'status': 'error', 'message': 'Geçersiz istek methodu'})


    