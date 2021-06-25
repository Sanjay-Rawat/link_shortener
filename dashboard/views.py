
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import loader
from django.http.response import HttpResponse
# Create your views here.
# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'dashboard.html', {'currentPage':'dashboard'})


def dashboard(request):
    # template = loader.get_template("about.html")
    # return HttpResponse(template.render())
    return render(request,'dashboard.html',{'currentPage':'dashboard'})
    

def xyz(request):
    # template = loader.get_template("contact.html")
    # return HttpResponse(template.render())
     return render(request,'contact.html',{'currentPage':'contact'})
