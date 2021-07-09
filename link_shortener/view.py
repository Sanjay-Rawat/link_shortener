
from home.models import UrlModel
from django.shortcuts import render
from django.http import HttpResponseRedirect

def invalidPath(request):
     return render(request,'404.html')

def redirectToHome(request):
    return HttpResponseRedirect("/home")


def getUrl(request,uid):
     # return HttpResponseRedirect("/home")
     try :
          result=UrlModel.objects.get(_id=uid)
          url=result.o_url
          return HttpResponseRedirect(url)
     except :
          return render(request,'404.html')
