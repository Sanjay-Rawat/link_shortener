
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import loader
from django.http.response import HttpResponse
# Create your views here.
# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'dashboard.html', context=None)


def dashboard(request):
    template = loader.get_template("dashboard.html")
    return HttpResponse(template.render())
