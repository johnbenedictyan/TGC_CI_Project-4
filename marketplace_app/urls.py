from django.conf.urls import url

from django.conf import settings # new
from django.conf.urls.static import static # new
from .views import marketplace,favourite_listings,listingcreator,listingeditor,categories,single_listing,my_listings,delete_listing,favourite

urlpatterns = [
    url(r'^$', marketplace, name="marketplace_link"),
    url(r'^favourites/$', favourite_listings, name="favourite_listings_link"),
    url(r'^listing/creator/$', listingcreator, name="listingcreator_link"),
    url(r'^listing/editor/(?P<listing_id>\d+)$', listingeditor, name="listingeditor_link"),
    url(r'^listing/categories/(?P<category_id>\d+)$', categories, name="categories_link"),
    url(r'^listing/single/(?P<listing_id>\d+)$',single_listing, name="single_listing_link"),
    url(r'^listing/delete/(?P<listing_id>\d+)$',delete_listing, name="delete_listing_link"),
    url(r'^my_listings/$', my_listings, name="my_listings_link"),
    url(r'^listing/single/(?P<listing_id>\d+)/favourite/$',favourite, name="favourite_link"),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)