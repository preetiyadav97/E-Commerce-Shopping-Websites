from django.shortcuts import render,HttpResponse,redirect
from Buy.admin import Contact,Image
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# ---- import for send email -----
from django.core.mail import send_mail

# ---- END -------


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
    data=Image.objects.all()
    show={'data':data}
    return render(request,'products.html',show)

def single(request):
    return render(request,'single-product.html')
    
def nav(request):
    return render(request,'nav.html')

def signup(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        gender=request.POST['gender']
        passward=request.POST['passward']
        confirmpassward=request.POST['confirmpassward']
        user = User.objects.create_user(username,email,passward)
        user.first_name=fname
        user.last_name=lname
        user.save()
        return redirect("index1")
    return render(request,'sign.html')

def login_detail(request):
    if request.method == 'POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user = authenticate(username=loginusername, passward=loginpassword)
    
        if user is not None:
            login(request,user)
        else:
           return HttpResponse('Not - found pages')
    return render(request,'login.html')

def logout_detail(request):
    logout(request)
    return render(request,'sign.html')