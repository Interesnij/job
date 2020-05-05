from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include ('main.urls')),
    path(r'^works/$', include ('works.urls')),
    path(r'^gallery/$', include ('gallery.urls')),
    path(r'^shop/$', include ('shop.urls')),
    path(r'^news/$', include ('news.urls')),
]
