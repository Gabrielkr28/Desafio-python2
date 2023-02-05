from django.urls import include, re_path
from Customer import views

urlpatterns=[
    re_path(r'^customer$', views.customerApi),
    re_path(r'^customer/([0-9]+)$', views.customerApi),

    re_path(r'^vehicle$', views.vehicleApi),
    re_path(r'^vehicle/([0-9]+)$', views.vehicleApi)
]
    