from django.conf.urls import url, include
from main.views import MainPageView, PagesView, AboutView


urlpatterns = [
	url(r'', MainPageView.as_view(), name="main"),
	url(r'pages/', PagesView.as_view()),
	url(r'about/', AboutView.as_view()),
]
