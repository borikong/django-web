from django.urls import path
from django.contrib import admin
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

app_name='main'

### 실제 링크명에 들어갈 문자 , views.py에서 정의한 함수명, html에서  app_name:name=?? 으로 불러올 이름
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog/<int:pk>',posting,name='posting'),
    path('<str:pk>/',categorized,name='categorized'),
    path('writing',writing,name='writing'),
    path('home',home,name='home'),
    path('blog/delete/<int:pk>',delete,name='delete')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)