from django.contrib import admin
from django.urls import path
from .views import index,about,contact,product,single,signup,login_detail,logout_detail,nav


urlpatterns = [
    path('index/',index,name="index1"),
    path('contact/',contact),
    path('about/',about),
    path('product/',product),
    path('single/',single),
    path('signup/',signup),
    path('login/',login_detail),
    path('logout/',logout_detail),
    path('nav/',nav)
   
]