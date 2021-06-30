from django.conf.urls import url
from django.urls.conf import path
from home.views import about,home,contact,saveContact

urlpatterns = [
    path('', home),
    path('contact/', contact), 
    path('about/', about),
    path('abc/', saveContact),
]