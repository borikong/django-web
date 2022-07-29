from django.urls import path
from django.contrib import admin
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name='main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog/<int:pk>',posting,name='posting'),
    path('categorized/<str:pk>',categorized,name='categorized'),
    path('<str:pk>/',categorized,name='categorized')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
