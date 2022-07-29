from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    CATEGORIES = (
        ('PYTHON/DJANGO', 'python/django'),
        ('JAVA/SPRING', 'java/spring'),
        ('ANDROID', 'android'),
        ('ML', 'ml'),
        ('PS', 'ps'),
        ('ETC', 'etc')
    )

    category = models.CharField(max_length=200, default="etc", choices=CATEGORIES)
    postname=models.CharField(max_length=50)
    contents=models.TextField()
    mainphoto=models.ImageField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.postname

    def summary(self):
        return self.contents[:100]