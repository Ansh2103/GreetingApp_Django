from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.core import serializers
from .models import card
import json



# class GreetingView(View):
#     def get(self, request):
      
#         greeting_qs = card.objects.all()
#         dict_ = {}
#         greeting_qs = [ dict_[name] for name in greeting_qs]
#         print(greeting_qs)
#         data = serializers.serialize("json", greeting_qs)
#         print(data)
#         return HttpResponse(data)

#Create your views here.
def home(request):
    context = {
        'name':'Shubham Kumar',
        'message':'Hello worlds'
    }
    return render(request,'index.html',context)
    
    #return HttpResponse('<h1>Hello World<h1>')

# def Card(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         message = request.POST.get('message')
#         Card = card(name=name,message=message)
#         Card.save()
#     return render(request,'index.html')

def about(request):
    return HttpResponse('<h1>Greeting Card App Home Page<h1>')

def services(request):
    return HttpResponse('<h1>Greeting Card App Services Page<h1>')

def contacts(request):
    return HttpResponse('<h1>Greeting Card App contacts Page<h1>')