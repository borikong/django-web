from django.urls import path,include

from django.contrib import admin
from django.urls import path, re_path

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('',include('main.urls')),
]

##urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
