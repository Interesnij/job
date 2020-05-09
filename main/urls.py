from django.conf.urls import url, include
from main.views import MainPageView, PagesView, AboutView, ApiPagesView


urlpatterns = [
	url(r'', MainPageView.as_view(), name="main"),
	url(r'pages/', PagesView.as_view()),
	url(r'^api/wp/v2/pages/', ApiPagesView.as_view()),
	url(r'about/', AboutView.as_view()),
]
