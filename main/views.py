from django.views.generic.base import TemplateView


class MainPageView(TemplateView):
	template_name = "main/mainpage.html"

class SettingsView(TemplateView):
	template_name = "main/settings.html"
