from django.shortcuts import HttpResponse


def register(request):
    return HttpResponse('hi this is register')

def login(request):
    return HttpResponse('hi this is login')

# Create your views here.
