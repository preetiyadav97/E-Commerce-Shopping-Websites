from django.shortcuts import render,HttpResponse,redirect
from Buy.admin import Contact,Category,Product,Cart,Wallet
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views import View
# ---- import for send messages -----
from django.contrib import messages
# ---- import for send email -----
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
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
        
        #--------
        # details={'name':name,'email':email,'mgs':mgs}
        # subject="Thanks for contacting"
        # html_message=render_to_string("contact.html",details)
        # plain_message=strip_tags(html_message)
        # from_email="k68146369@gmail.com"
        # to= "preetiyadav73703@gmail.com"

        # send_mail(subject,html_message=html_message,plain_message,from_email,to,fail_silently=False)
        send_mail(
          "Thanks for contacting",
           mgs,
          'settings.EMAIL_HOST_USER',
           ['preetiyadav73703@gmail.com'],
           fail_silently=False,
        )
    return render(request,'contact.html')

def index(request):
    man_products=Product.objects.filter(cat__name="Men")
    woman_products=Product.objects.filter(cat__name="women's")
    kid_products=Product.objects.filter(cat__name="Kids")
    user=request.user
    a = user.id
    quantity=Cart.objects.filter(user=a).count()
    return render(request,'index.html',{'man_products':man_products,'woman_products':woman_products,'kid_products':kid_products,'quantity':quantity})
     

def product(request):
    man_products=Product.objects.filter(cat__name="Men",permission=True)
    woman_products=Product.objects.filter(cat__name="women's",permission=True)
    kid_products=Product.objects.filter(cat__name="Kids",permission=True)
    # per=Product.objects.filter(permission=True)
    return render(request,'products.html',{'man_products':man_products,'woman_products':woman_products,'kid_products':kid_products})


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
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']

        user = User.objects.create_user(username,email,password)
        user.first_name=fname
        user.last_name=lname

        user.save()
        return redirect("index1")

    return render(request,'sign.html')

# def login_detail(request):
#     # print("Login")
#     if request.method =="POST":
#         print("Login")
#         loginusername=request.POST['loginusername']
#         print(loginusername)
#         loginpassword=request.POST['loginpassword']
#         print(loginpassword)
#         user = authenticate(username=loginusername, passward=loginpassword)
#         print(user)
    
#         if user is not None:
#             login(request,user)
#             return redirect("index1")
#         else:
#            return HttpResponse('Not - found pages')
#     return render(request,'login.html')

def login_detail(request):
    if request.method =="POST":
        username = request.POST["loginusername"]
        password = request.POST["loginpassword"]
        user = authenticate(username=username, password=password)
        print(user)
        print("==================================")
        if user is not None:
            login(request, user)
            return redirect("index1")
            
            
        else:
            return HttpResponse('Not - found pages')

    return render(request,'login.html')


def logout_detail(request):
    logout(request)
    man_products=Product.objects.filter(cat__name="Men")
    woman_products=Product.objects.filter(cat__name="women's")
    kid_products=Product.objects.filter(cat__name="Kids")
    return render(request,'index.html',{'man_products':man_products,'woman_products':woman_products,'kid_products':kid_products})
    # return render(request,'index.html')

def cart(request,pk):
    user=request.user
   
    a = user.id
    quantity=Cart.objects.filter(user=a).count()

 
    a=Cart(user_id=user.id,product_id=pk)
    a.save()
    dat=Cart.objects.filter(user=user.id)
    # dat=Cart.objects.all()
    show={'dat':dat,'quantity':quantity}
   

    return render(request,'single-product.html',show)


def cartshow(request):
    user=request.user
    a = user.id
    print(a)
    product=request.POST.get('product')
    dat=Cart.objects.filter(user=a)
    quantity=Cart.objects.filter(user=a).count()
    print(  quantity)
    # quan={'quantity':quantity}
    # print(quan)
    show={'dat':dat,'quantity':quantity}
    print(show)
   

    return render(request,'single-product.html',show)






