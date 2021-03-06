from django.conf.urls import url

from django.conf import settings # new
from django.conf.urls.static import static # new
from .views import login,register,logout,account_details

urlpatterns = [
    url(r'^login/$', login, name="login_link"),
    url(r'^register/$', register, name="register_link"),
    url(r'^logout/$', logout, name="logout_link"),
    url(r'^account_details/$', account_details, name="account_details_link"),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)