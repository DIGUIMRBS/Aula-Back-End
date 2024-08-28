from django.shortcuts import render

#create yous views here

from django.http import HttpResponse

def home(request):
    return render(request, 'todos/home.html');


# Create your views here.
