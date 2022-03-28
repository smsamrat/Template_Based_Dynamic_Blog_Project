
from . import views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('AppBlog.urls')),
    path('', include('AppAccount.urls')),
    path('',views.index, name='index')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
