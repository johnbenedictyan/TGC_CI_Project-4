from django.conf.urls import url

from django.conf import settings # new
from django.conf.urls.static import static # new

urlpatterns = [
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)