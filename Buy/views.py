from django.shortcuts import render,HttpResponse,redirect
from Buy.admin import Contact,Category,Product,Cart,Wallet
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
    man_products=Product.objects.filter(cat=5)
    woman_products=Product.objects.filter(cat=6)
    kid_products=Product.objects.filter(cat=7)

    show={'man_products':man_products}
    women={'woman_products':woman_products}
    kid={'kid_products':kid_products}
    return render(request,'products.html',show,women,kid)

def single(request):
    return render(request,'single-product.html')
    
def nav(request):
    return render(request,'show.html')

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
    if request.method =="POST":
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
    return render(request,'index.html')