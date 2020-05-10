from django.views.generic.base import TemplateView


class MainPageView(TemplateView):
	template_name='main/mainpage.html'

class Page1View(TemplateView):
	template_name='main/page_1.html'
