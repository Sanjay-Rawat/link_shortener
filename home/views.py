from django.db import models
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render
from django.contrib import messages
from home.models import ContactModel , UrlModel
import string
import random
from datetime import datetime
# Create your views here.


def home(request):
     return render(request,'home.html',{'currentPage':'home'})

def login(request):
     return render(request,'login.html',{'currentPage':'login'})

def signup(request):
     return render(request,'signup.html',{'currentPage':'signup'})

def about(request):
     return render(request,'about.html',{'currentPage':'about'})

def contact(request):
          if(request.method=='POST'):
               return saveContact(request)
          data= getContacts()
          return render(request,'contact.html',{'currentPage':'contact','contacts':data})

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
               return HttpResponse("form is submitted") #https://pypi.org/project/mysqlclient/


def getContacts():
     # return ContactModel.objects.get(email='sanjay96rawat@gmail.com')
     return ContactModel.objects.all()




def shortUrl(request):
     # o_url = 'https://www.programiz.com/python-programming/datetime/current-datetime'
     o_url = request.POST.get('url')
     created_at = datetime.now()
     uid = short_random_string(6)
     result =UrlModel(_id=uid, o_url=o_url ,created_at=created_at)
     result.save()
     return HttpResponse('http://127.0.0.1:8000/'+uid)

     
     



def short_random_string(N:int) -> str:
    return ''.join(random.SystemRandom().choice(
        string.ascii_letters + \
        string.digits) for _ in range(N)
    )




