from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('terms&conditions', views.away), 
    path('archieve', views.archieve),
    # path('test', views.test,)
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)