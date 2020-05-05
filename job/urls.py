from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', include ('main.urls')),
    url(r'^works/$', include ('works.urls')),
    url(r'^gallery/$', include ('gallery.urls')),
    url(r'^shop/$', include ('shop.urls')),
    url(r'^news/$', include ('news.urls')),
]
