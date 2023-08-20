from django.shortcuts import render,HttpResponse,redirect
from Buy.admin import Contact

# Create your views here.
def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        mgs=request.POST['message']
        detail=Contact(name=name,email=email,mgs=mgs)
        detail.save()
    return render(request,'contact.html')

def index(request):
    return render(request,'index.html')

def product(request):
    return render(request,'products.html')

def single(request):
    return render(request,'single-product.html')