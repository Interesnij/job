from django.conf.urls import url, include
from main.views import MainPageView, Page1View


urlpatterns = [
	url(r'', MainPageView.as_view(), name="main"),
	url(r'^frans-blijft-thuis/$', Page1View.as_view(), name="test"),
]
