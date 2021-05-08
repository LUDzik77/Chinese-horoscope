from django.http import HttpResponse
from django.shortcuts import render
from divinations.models import Divination  #i might do it in wrong file /  also can be  a name issue 
from zodiacs.models import Zodiac
from .forms import GiveYearForm
from datetime import datetime

def home_view(request, *args, **kwargs):
    all_zodiacs = Zodiac.objects.all()
    my_context =  {}
    for zodiac_ in range(len (all_zodiacs)):
        my_context[zodiac_+1] =  all_zodiacs[zodiac_]
    return (render(request, "index.html", my_context ))
    
def zodiac_page_view(request, id_, *args, **kwargs):
    now = datetime.now()
    day_date = now.strftime("%d %b %Y") 
    day_ = int(now.strftime("%d"))
    month_ = int(now.strftime("%m"))

    obj_dev = devination_for_a(day_, month_, id_)
    obj_zod = Zodiac.objects.get(id=id_) 
    my_context = {
        'description': obj_dev.description,
        'day_date': day_date,
        'zodiac_sign': obj_zod,   
    }
    return (render(request, "zodiac_page.html", my_context))

# it is not a view but for clarity this funtion is below the zodiac_page_view
def devination_for_a(day, month, zodiac_id):
    all_divination = Divination.objects.all()
    base_number = day*month*zodiac_id
    wynik = base_number%len(all_divination) 
    return (all_divination[wynik])    
       
    
def contact_page_view(request, *args, **kwargs):
    return (render(request, "contact.html", {}))    

# T E S T
def zodiac_create_view(request, *args, **kwargs):
    if request.method == "POST":
        now = datetime.now()
        day_date = now.strftime("%d %b %Y")        
        zodiac_ = request.POST.get('Zodiac')
        obj_dev = Divination.objects.get(id=5)
        obj_zod = Zodiac.objects.get(id=zodiac_)         
        my_context = {
            'description': obj_dev.description,
            'day_date': day_date,
            'zodiac_sign': obj_zod,   
        }        
        
        #if user == "mark":
            #return HttpResponse('hello mark')
    return (render(request, "zodiac_page.html", my_context))


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

