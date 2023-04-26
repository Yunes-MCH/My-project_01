from django.contrib.auth.models import User
from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name
class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='items',on_delete=models.CASCADE)
    description = models.TextField(blank=True,null=True)
    #price = models.FloatField()
    image = models.ImageField(upload_to='item_images',blank=True,null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Logo(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='logos',on_delete=models.CASCADE)
    #description = models.TextField(blank=True,null=True)
    #price = models.FloatField()
    image = models.ImageField(upload_to='logo_images',blank=True,null=True)
    #is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name='logos',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

         

# Create your models here.
