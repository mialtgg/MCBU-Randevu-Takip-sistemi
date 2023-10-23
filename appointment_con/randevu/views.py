import datetime
import json
from pyexpat.errors import messages
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Events
from .forms import RandevuForm
from django.http import HttpResponse, JsonResponse
from datetime import datetime

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










