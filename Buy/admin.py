from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    model=Contact
    list_display=['name','email','mgs']
admin.site.register(Contact,ContactAdmin)