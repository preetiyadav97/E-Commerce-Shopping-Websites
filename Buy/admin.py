from django.contrib import admin
from .models import Contact,Category,Product,Cart,Wallet
# Register your models here.

# Contact-------

class ContactAdmin(admin.ModelAdmin):
    model=Contact
    list_display=['name','email','mgs']
admin.site.register(Contact,ContactAdmin)

# Category-------

admin.site.register(Category)

# Produc-------

class ProductAdmin(admin.ModelAdmin):
    model=Product
    list_display=['name','price','image']
admin.site.register(Product,ProductAdmin)

#  Cart-------


admin.site.register(Cart)

# Wallet------


class WalletAdmin(admin.ModelAdmin):
    model=Wallet
    list_display=['user','amount']
admin.site.register(Wallet,WalletAdmin)