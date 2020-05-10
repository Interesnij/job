from django.conf.urls import url
from gallery.views import *


urlpatterns = [
    url(r'^$', GalleryView.as_view(), name='gallery'),
]
