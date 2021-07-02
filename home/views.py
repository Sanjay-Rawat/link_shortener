from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render
from django.contrib import messages
from home.models import ContactModel
# Create your views here.


def home(request):
     return render(request,'home.html',{'currentPage':'home'})

def about(request):
     return render(request,'about.html',{'currentPage':'about'})

def contact(request):
          if(request.method=='POST'):
               return saveContact(request)
          return render(request,'contact.html',{'currentPage':'contact'})

def saveContact(request):
               a = request.POST.get('name')
               b = request.POST.get('email')
               c = request.POST.get('contactNumber')
               d = request.POST.get('comment')
               data = ContactModel(
                    name=a ,
                    email=b,
                    contactNumber=c,
                    comment=d
                    )
               data.save()
               return HttpResponse("form is submitted")
