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
               name = request.POST.get('name')
               email = request.POST.get('email')
               contactNumber = request.POST.get('contactNumber')
               comment = request.POST.get('comment')
               data = ContactModel(
                    name=name ,
                    email=email,
                    contactNumber=contactNumber,
                    comment=comment
                    )
               data.save()
               return HttpResponse("form is submitted")
