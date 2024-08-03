from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(default="bala(Default)",max_length=50,null=True)
    title=models.CharField(default="bala(Default)",max_length=50,null=True)
    desc_text="nothin about me"
    desc=models.CharField(default=desc_text,max_length=400,null=True)
    profile_img=models.ImageField(null=True,blank=True,upload_to="image")
    def __str__(self):
        return self.name