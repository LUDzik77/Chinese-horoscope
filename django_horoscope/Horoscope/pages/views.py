from django.http import HttpResponse
from django.shortcuts import render
from divinations.models import Divination  #i might do it in wrong file /  also can be  a name issue 
from zodiacs.models import Zodiac
from .forms import GiveYearForm
#from datetime import datetime, timedelta, date
from datetime import datetime
from datetime import timedelta

def home_view(request, *args, **kwargs):
    all_zodiacs = Zodiac.objects.all()
    my_context =  {}
    for zodiac_ in range(len (all_zodiacs)):
        my_context[zodiac_+1] =  all_zodiacs[zodiac_]
    return (render(request, "index.html", my_context ))
    
def zodiac_page_view(request, id_, *args, **kwargs):
    now = datetime.now()
    tomorrow = now + timedelta(days=1)
    after_tomorrow = now + timedelta(days=2)   
     
    day_today = int(now.strftime("%d"))
    month_today = int(now.strftime("%m"))
    day_tomorrow = int(tomorrow.strftime("%d"))
    month_tomorrow = int(tomorrow.strftime("%m"))
    day_after_tomorrow = int(after_tomorrow.strftime("%d"))
    month_after_tomorrow = int(after_tomorrow.strftime("%m"))    

    obj_dev1 = devination_for_a(day_today, month_today, id_)
    obj_dev2 = devination_for_a(day_tomorrow, month_tomorrow, id_)
    obj_dev3 = devination_for_a(day_after_tomorrow, month_after_tomorrow, id_)
    
    day1 = now.strftime("%d %b %Y") 
    day2 = tomorrow.strftime("%d %b %Y")
    day3 =  after_tomorrow.strftime("%d %b %Y") 
    obj_zod = Zodiac.objects.get(id=id_) 
    my_context = {
        'description1': obj_dev1.description,
        'description2': obj_dev2.description,
        'description3': obj_dev3.description,
        'day_today': day1,
        'day_tomorrow': day2,
        'day_after_tomorrow': day3,
        'zodiac_sign': obj_zod,   
    }
    return (render(request, "zodiac_page.html", my_context))

# it is not a view but for clarity this funtion is below the zodiac_page_view
def devination_for_a(day, month, zodiac_id, ):
    all_divination = Divination.objects.all()
    base_number = day*month*zodiac_id
    wynik = base_number%len(all_divination) 
    return (all_divination[wynik])    
       
    
def contact_page_view(request, *args, **kwargs):
    return (render(request, "contact.html", {}))

def game_page_view(request, *args, **kwargs):
    return (render(request, "game.html", {}))   




#def zodiac_create_view(request, *args, **kwargs):
    #if request.method == "POST":
        #now = datetime.now()
        #day_date = now.strftime("%d %b %Y")        
        #zodiac_ = request.POST.get('Zodiac')
        #obj_dev = Divination.objects.get(id=5)
        #obj_zod = Zodiac.objects.get(id=zodiac_)         
        #my_context = {
            #'description': obj_dev.description,
            #'day_date': day_date,
            #'zodiac_sign': obj_zod,   
        #}        
        
        ##if user == "mark":
            ##return HttpResponse('hello mark')
    #return (render(request, "zodiac_page.html", my_context))


def test_form(request, *args, **kwargs):
    if request.method == "POST":
        user = request.POST.get('username')
        if user == "mark":
            return HttpResponse('hello mark')
    return render(request, "form.html")
    #return render(request, "zodiac_page.html")


