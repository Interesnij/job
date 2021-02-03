from django.conf.urls import url
from works.views import *


urlpatterns = [
    url(r'^$', WorksView.as_view(), name='works'),
] 
