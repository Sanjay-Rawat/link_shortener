from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render
from django.contrib import messages
# Create your views here.


def home(request):
     return render(request,'home.html',{'currentPage':'home'})

def about(request):
     return render(request,'about.html',{'currentPage':'about'})

def contact(request):
          return render(request,'contact.html',{'currentPage':'contact'})

def saveContact(request):
               name = request.POST.get('name')
               print(name)
               return HttpResponse("form is submitted")
