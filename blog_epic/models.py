from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings

# Create your models here.

class post_class(models.Model):
    
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200, default="Placeholder Subtitle")  #null = True and blank = True for further flexibility
    text = models.TextField()
    img = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    blank=True,
    null=True,)

    def __str__(self):
        return self.title