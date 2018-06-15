from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
# function based view
def home(request):
    #return HttpResponse('hello ajit')
    num=random.randint(0,9846784698)
    return render(request,'home.html',{"context":False,"num":num}) #response

def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})