
from django.shortcuts import render
from django.http import HttpResponseRedirect

def invalidPath(request):
     return render(request,'404.html')

def redirectToHome(request):
    return HttpResponseRedirect("/home")
