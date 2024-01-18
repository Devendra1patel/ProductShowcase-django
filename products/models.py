from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = HTMLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name
    
class myContact(models.Model):
    serial_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=17)
    address = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    order = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class myImages(models.Model):
    image = models.ImageField(upload_to= 'product_myImages/')
    time = models.TimeField(auto_created=True)

class about(models.Model):
    about_description = HTMLField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    indiamart_link = models.URLField(blank=True, null=True)
    other_social_links = models.TextField(blank=True, null=True)




