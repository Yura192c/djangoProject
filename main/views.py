from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'main/registration.html')


def about(request):
    return HttpResponse('<h4>About page<h4>')