from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse('hi this is index')

def about(request):
    return HttpResponse('this is about')

def contact(request):
    return HttpResponse('this is contact')
# Create your views here.
