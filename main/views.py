from django.views.generic.base import TemplateView
from .main_data import data
from .about_data import about
from django.views import View
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse


class MainPageView(TemplateView):
	template_name='main/test.html'


class PagesView(View):
	def get(self,request,*args,**kwargs):
		my_data = data
		return my_data


class AboutView(View):
	def get(self,request,*args,**kwargs):
		my_data = about
		return JsonResponse(my_data)
