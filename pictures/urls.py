from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns=[
    path('',views.welcome, name = 'welcome'),
    path('search/',views.search_image,name='search_image'),
    path('location/',views.get_image_by_location,name='location'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)