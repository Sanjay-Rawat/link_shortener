from django.shortcuts import render
from django.template import loader
from django.http.response import HttpResponse

# Create your views here.
def about(request):
    # template = loader.get_template("about.html")
    return render(request,'about.html',{'currentPage':'about'})