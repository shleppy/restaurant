from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

@login_required
def management(request):
    """Main management page"""
    return render(request, 'restaurant/management.html')


def customers(request):
    return HttpResponse("Customer management")


def customer(request, customer_id):
    return HttpResponse("Hello, this is the info about customer %s" % customer_id)


