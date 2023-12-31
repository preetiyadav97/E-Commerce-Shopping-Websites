from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=400)
    email=models.EmailField()
    mgs=models.TextField()
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=500)
    price=models.FloatField(null=True,blank=True)
    image=models.ImageField(upload_to="static/assets/img")
    permission=models.BooleanField(default=False,null=None,blank=None)
    

    def __str__(self):
        return self.name



class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_cart')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_cart')
    # product_qty=models.IntegerField()
    # created_at=models.DateTimeField()
    
    # def __str__(self):
    #     return self.user.name

    
    

class Wallet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.user
    

# rzp_test_Q7haYLxCb3o990 id 
# JycshNrSiVs8mv6z6mRXy6HK secret

    
# class Image(models.Model):
#     name=models.CharField(max_length=500)
#     price=models.FloatField(null=True, blank=True)
#     image=models.ImageField(upload_to="static/assets/img")
#     # rating = models.IntegerField(default=0)

#     def __str__(self):
#         return self.name


    

