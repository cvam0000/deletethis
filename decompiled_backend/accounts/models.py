# from django.db import models

# # Create your models here.

# from django.contrib.auth.models import User


# class Profile(models.Model):
#     user= models.OneToOneField(User,on_delete=models.CASCADE)
#     pic=models.ImageField()




from django.db import models

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)