from django.contrib import admin
from django.urls import path
from .views import index,about,contact,product,single


urlpatterns = [
    path('index/',index),
    path('contact/',contact),
    path('about/',about),
    path('product/',product),
    path('single/',single)
   
]