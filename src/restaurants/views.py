from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
import random

# Create your views here.
# function based view
def home(request):
    #return HttpResponse('hello ajit')
    num=random.randint(0,9846784698)
    return render(request,'home.html',{"context":False,"num":num}) #response

class HomeView(TemplateView):
    template_name="home.html"
    def get_context_data(self,*args,**kwargs):
        context = super(HomeView, self).get_context_data(*args,**kwargs)
        data=False
        num=random.randint(0,9846784698)
        context={
            'data':data,
            'num':num
        }
        return context

class ContactView(TemplateView):
    template_name="contact.html"

class AboutView(TemplateView):
    template_name="about.html"