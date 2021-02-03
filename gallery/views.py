from django.views.generic.base import TemplateView
import json
from django.http import HttpResponse
from data import _array
from django.views import View


class GalleryView(TemplateView):
    template_name = "gallery.html"


class GalleryJson(View):
    def get(self, request, **kwargs):
        return HttpResponse(json.dumps({"_array": _array}))
