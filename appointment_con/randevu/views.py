import datetime
import json
from pyexpat.errors import messages
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Events
from .forms import RandevuForm
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
# def randevu(request):
#     print("12233")
#     if request.method == "POST":
#         print("1")
#         form =RandevuForm(request.POST)
#         print(form)
#         if form.is_valid():
#             print("2")
#             form.save()
#             messages.success(request,form.errors)
#             return redirect ('randevu')
#         else:
#            print(form.errors)
#            messages.error(request,form.errors)
#     else :
#         print('9')
#         form=RandevuForm()
#     return render(request,'randevu/randevu.html',{'form':form}) 
# endpoint için
def get_events(request):
    events = Events.objects.all().values()
    return JsonResponse(list(events), safe=False)


def calendar(request):
    all_events = Events.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'randevu/randevu.html',context)

def all_events(request):                                                                                                 
    all_events = Events.objects.all()                                                                               
    out = []                                                                                                             
    for event in all_events:   
        print(event.date)
        times=event.date                                                                          
        out.append({ 
            'id': event.id,
            'name': event.name,
            'description': event.description,
            'priority': event.get_priority_display(),  # Öncelik değerini okunabilir şekilde alıyoruz
            'date': event.date,
            'all_day': event.all_day,
            'start_time': event.start_time.strftime("%H:%M:%S") if event.start_time else None,
            'end_time': event.end_time.strftime("%H:%M:%S") if event.end_time else None,                                                                                                    

        })                                                                                                               
                                                                                                                     
    return JsonResponse(out, safe=False)  

def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    if start is None or end is None or title is None:
        error_message = "Tüm alanlar doldurulmalıdır."
        return JsonResponse({"error": error_message})
    else : 
       event = Events(name=str(title), start=start, end=end)
       event.save()
       data = {}
       return JsonResponse(data)




def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)


def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)



# def event(request):
#     all_events = Events.objects.all()
#     get_event_types = Events.objects.only('event_type')

#     # if filters applied then get parameter and filter based on condition else return object
#     if request.GET:  
#         event_arr = []
#         if request.GET.get('event_type') == "all":
#             all_events = Events.objects.all()
#         else:   
#             all_events = Events.objects.filter(event_type__icontains=request.GET.get('event_type'))

#         for i in all_events:
#             event_sub_arr = {}
#             event_sub_arr['title'] = i.event_name
#             start_date = datetime.datetime.strptime(str(i.start_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
#             end_date = datetime.datetime.strptime(str(i.end_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
#             event_sub_arr['start'] = start_date
#             event_sub_arr['end'] = end_date
#             event_arr.append(event_sub_arr)
#         return HttpResponse(json.dumps(event_arr))

#     context = {
#         "events":all_events,
#         "get_event_types":get_event_types,

#     }
#     return render(request,'admin/poll/event_management.html',context)




@csrf_exempt  # CSRF korumasını devre dışı bırakmak için kullanabilirsiniz, güvenlik gereksinimlerinize bağlıdır
@require_POST  # Sadece POST isteklerini kabul etmek için kullanılır
def add_event(request):
    if request.method == 'POST':
        try:
             # JSON veriyi işleme
            data = json.loads(request.body)
            print(data)
            date_string_start = data.get('start')
            date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
            parsed_date = datetime.strptime(date_string_start, date_format)
            date1 = parsed_date.date()  # Sadece tarih
            time1 = parsed_date.time()  # Sadece saat

            date_string_end = data.get('end')
            date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
            parsed_date = datetime.strptime(date_string_end, date_format)
            date2 = parsed_date.date()  # Sadece tarih
            time2 = parsed_date.time()  # Sadece saat


            response_data = {
        'date': date1,
        'time': time1,
        
       
    }
            print(response_data)
      




            
            # Etkinlik bilgilerini alın



            title = data.get('title')
            description = data.get('description')
            priority = data.get('className')
            if(priority=="bg-danger-subtle"):
                priority="Yüksek"
            date = date1
            all_day = data.get('allDay')
            start_time = time1
            end_time = time2
            location = data.get('location')

            # Etkinliği veritabanına kaydedin
            event = Events(
                name=title,
                description=description,
                priority=priority,
                date=date,
                all_day=all_day,
                start_time=start_time,
                end_time=end_time,
                location=location
            )

    #         date_string = data.get('start')
    #         date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    #         parsed_date = datetime.strptime(date_string, date_format)
    #         year = parsed_date.year
    #         month = parsed_date.month
    #         day = parsed_date.day
    #         hour = parsed_date.hour
    #         minute = parsed_date.minute
    #         date = parsed_date.date()  # Sadece tarih
    #         time = parsed_date.time()  # Sadece saat
            

    #         response_data = {
    #     'year': year,
    #     'month': month,
    #     'day': day,
    #     'hour': hour,
    #     'minute': minute,
       
    # }
    #         print(response_data)
     
            event.save()
            

            return JsonResponse({'message': 'Etkinlik başarıyla kaydedildi'})
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON verisi işlenemedi'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)









