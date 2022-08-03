from django.contrib import admin
from .models import Post,myinfo

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=(
            'category',
            'postname',
            'hits',
            'mainphoto',
            'subphoto1',
            'subphoto2',
            'subphoto3',
            'subphoto4',
            'subphoto5',
            'subphoto6',
            'subphoto7',
            'subphoto8',
            'subphoto9',
            'created_at',
            'updated_at')

admin.site.register(Post,PostAdmin)
admin.site.register(myinfo)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     post_fields=('contents',)
#     list_display=(
#         'category',
#         'postname',
#         'hits',
#         'mainphoto',
#         'subphoto1',
#         'subphoto2',
#         'subphoto3',
#         'subphoto4',
#         'subphoto5',
#         'subphoto6',
#         'subphoto7',
#         'subphoto8',
#         'subphoto9',
#         'created_at',
#         'updated_at'
#     )
#     list_display_links=list_display