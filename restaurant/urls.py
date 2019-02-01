from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.customers, name='customers'),
    path('customers/<int:customer_id>/', views.customer, name='customer')
]
