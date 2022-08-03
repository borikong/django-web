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

    category = models.CharField(max_length=200, default="etc", choices=CATEGORIES,verbose_name="글 분류")
    user=models.CharField(max_length=20, default="borikong",verbose_name="작성자")
    passwd=models.CharField(max_length=50,default="",verbose_name="비밀번호")
    postname=models.CharField(max_length=100,verbose_name="제목")
    contents=models.TextField(verbose_name="내용")
    hits=models.PositiveIntegerField(default=0,verbose_name="조회수")
    mainphoto=models.ImageField(blank=True,null=True)
    subphoto1=models.ImageField(blank=True, null=True)
    subphoto1 = models.ImageField(blank=True, null=True)
    subphoto2 = models.ImageField(blank=True, null=True)
    subphoto3 = models.ImageField(blank=True, null=True)
    subphoto4 = models.ImageField(blank=True, null=True)
    subphoto5 = models.ImageField(blank=True, null=True)
    subphoto6 = models.ImageField(blank=True, null=True)
    subphoto7 = models.ImageField(blank=True, null=True)
    subphoto8 = models.ImageField(blank=True, null=True)
    subphoto9 = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.postname

    def summary(self):
        return self.contents[:100]

class myinfo(models.Model):
    education = models.CharField(max_length=100)
    workExperience = models.TextField()
