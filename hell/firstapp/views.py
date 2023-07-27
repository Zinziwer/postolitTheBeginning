from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

# Create your views here.
def index(request):
    return HttpResponse("index>")
def about(request):
    return HttpResponse("About")
def contact(request):
    return HttpResponseRedirect("/about")
def details(request):
    return HttpResponsePermanentRedirect('/')
def products(request, productid=1):
    output = "<h2>Product № {0}</h2>".format(productid)
    return HttpResponse(output)
def users(request, id=1, name='Maxim'):
    output = "<h2>User</h2><h3>id № {0} Name: {1}</h3>".format(id, name)
    return HttpResponse(output)
