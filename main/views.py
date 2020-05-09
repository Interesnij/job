from django.views.generic.base import TemplateView
from .main_data import data
from .about_data import about
from django.views import View
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView


class MainPageView(TemplateView):
	template_name='main/mainpage.html'


class PagesView(TemplateView):
	template_name = "main/pages.html"
	def get(self,request,*args,**kwargs):
		self.my_data = data
		return super(PagesView,self).get(request,*args,**kwargs)

	def get_context_data(self, **kwargs):
		context = super(PagesView, self).get_context_data(**kwargs)
		context['data'] = data
		return context


class AboutView(View):
	def get(self,request,*args,**kwargs):
		my_data = about
		return JsonResponse(my_data)


class ApiPagesView(APIView):

	def get(self, request):
		return Response(data, status=status.HTTP_200_OK)
