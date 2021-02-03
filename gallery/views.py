from django.views.generic.base import TemplateView
import json
from django.http import HttpResponse
from django.views import View


class GalleryView(TemplateView):
    template_name = "gallery.html"


class GalleryJson(TemplateView):
    template_name = "gallery_json.html"
