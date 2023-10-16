from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Stock

# Create your views here.
def stocks(request):
    #return HttpResponse('<h1>Hello World ! You are at stocks index.</h1>')
    mystocks = Stock.objects.all().values()
    template = loader.get_template('all_stocks.html')
    context = {
        'stocks': mystocks,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mystock = Stock.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mystock' : mystock,
    }
    return HttpResponse(template.render(context, request))