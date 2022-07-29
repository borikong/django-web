from django.urls import path
from django.contrib import admin
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name='main'

### 실제 링크명에 들어갈 문자 , views.py에서 정의한 함수명, html에서  app_name:name=?? 으로 불러올 이름
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog/<int:pk>',posting,name='posting'),
    path('<str:pk>/',categorized,name='categorized'),
    path('writing',writing,name='writing')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
