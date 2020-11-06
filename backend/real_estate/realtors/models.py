from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    website_url = models.CharField(max_length=200,null=True,blank=True)
    linkedin_url = models.CharField(max_length=200,null=True,blank=True)
    twitter_url = models.CharField(max_length=200,null=True,blank=True)
    facebook_url = models.CharField(max_length=200,null=True,blank=True)
    top_seller = models.BooleanField(default=False)
    date_hired = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.name