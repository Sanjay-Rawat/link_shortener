from django.conf.urls import url
from django.urls.conf import path
from home.views import about,home,contact

urlpatterns = [
    path('', home),
    path('contact/', contact), 
    path('about/', about),
]