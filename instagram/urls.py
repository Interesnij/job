from django.conf.urls import url
from instagram.views import *


urlpatterns = [
    url(r'^$', InstagramView.as_view(), name='instagram'),
]
