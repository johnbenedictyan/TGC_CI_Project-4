from django.conf.urls import url

from django.conf import settings # new
from django.conf.urls.static import static # new

from .views import main_page,test_page,test_function

urlpatterns = [
    url(r'^$', main_page, name="main_page_link"),
    url(r'^test/$', test_page, name="test_page_link"),
    url(r'^test_function/$', test_function, name="test_function_link"),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)