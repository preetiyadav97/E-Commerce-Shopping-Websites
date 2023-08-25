from django.contrib import admin
from django.urls import path
from .views import index,about,contact,product,single,signup,login_detail,logout_detail,nav


urlpatterns = [
    path('index/',index,name="index1"),
    path('contact/',contact,name="contact1"),
    path('about/',about,name="about1"),
    path('product/',product,name="product1"),
    path('single/',single,name="single1"),
    path('signup/',signup,name="signup1"),
    path('login/',login_detail,name="login1"),
    path('logout/',logout_detail,name="logout1"),
    path('nav/',nav)
   
]