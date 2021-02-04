from django.views.generic.base import TemplateView
import json
from django.http import HttpResponse
from django.views import View
from .data import *


class GalleryView(TemplateView):
    template_name = "gallery.html"


class GalleryJson(View):
    def get(self, request, **kwargs):
        return HttpResponse(json.dumps(data))
