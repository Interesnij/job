from django.views.generic.base import TemplateView
from ad_categories.models import AdCategory
from skill_categories.models import SkillCategory


class MainPageView(TemplateView):
	template_name = "main/mainpage.html"

class Page1View(TemplateView):
	template_name = "main/page1.html"
