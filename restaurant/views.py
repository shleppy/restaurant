from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello welcome to our management page!")


def customers(request):
    return HttpResponse("Customer management")


def customer(request, customer_id):
    return HttpResponse("Hello, this is the info about customer %s" % customer_id)


