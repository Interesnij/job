from django.conf.urls import url, include
from main.views import MainPageView, SettingsView


urlpatterns = [
	url(r'^$', MainPageView.as_view(), name="main"),
	url(r'^settings/$', SettingsView.as_view(), name="settings"),
]
