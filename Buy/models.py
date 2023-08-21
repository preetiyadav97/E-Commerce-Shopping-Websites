from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=400)
    email=models.EmailField()
    mgs=models.TextField()
    
    def __str__(self):
        return self.name

class Image(models.Model):
    name=models.CharField(max_length=500)
    price=models.FloatField(null=True, blank=True)
    image=models.ImageField(upload_to="static/assets/img")
    # rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name


    

