from django.conf.urls import url
from news.views import *


urlpatterns = [
    url(r'^$', NewsView.as_view(), name='news'),
]
