from django.contrib import admin
from .models import Contact,Image
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    model=Contact
    list_display=['name','email','mgs']
admin.site.register(Contact,ContactAdmin)

class ImageAdmin(admin.ModelAdmin):
    model=Image
    list_display=['name','price','image']
admin.site.register(Image,ImageAdmin)