from django.db import models
from django.contrib.auth.models import User
class Image(models.Model):
    name = models.CharField(max_length=255)
    #description = models.TextField(blank=True,null=True)
    #price = models.FloatField()
    image = models.ImageField(upload_to='image_images',blank=True,null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name='images',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField( User,on_delete=models.CASCADE,null=True,blank=True)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

# Create your models here.
