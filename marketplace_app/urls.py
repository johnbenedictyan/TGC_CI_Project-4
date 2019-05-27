from django.conf.urls import url

from django.conf import settings # new
from django.conf.urls.static import static # new
from .views import marketplace

urlpatterns = [
    url(r'^$', marketplace, name="marketplace_link"),
    
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)