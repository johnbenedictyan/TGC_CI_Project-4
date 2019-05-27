from django.conf.urls import url

from django.conf import settings # new
from django.conf.urls.static import static # new
from .views import product_details

urlpatterns = [
    url(r'^(?P<product_id>\d+)$', product_details, name="product_details_link"),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)