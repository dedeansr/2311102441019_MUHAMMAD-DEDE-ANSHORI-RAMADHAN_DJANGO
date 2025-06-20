from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from resume.views import home, about

from django.contrib import admin
    
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name="home"),
    path('dashboard/', include("berita.urls")),

]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)