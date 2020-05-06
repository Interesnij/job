from django.views.generic.base import TemplateView
from main_page import data
from django.views import View
from django.http import HttpResponse


class MainPageView(TemplateView):
	template_name='main/test.html'


class MainPageView(View):
	def get(self,request,*args,**kwargs):
		my_data = data
		return data
