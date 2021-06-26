from django.shortcuts import render

# Create your views here.


def home(request):
     return render(request,'home.html',{'currentPage':'home'})

def about(request):
     return render(request,'about.html',{'currentPage':'about'})

def contact(request):
     return render(request,'contact.html',{'currentPage':'contact'})
