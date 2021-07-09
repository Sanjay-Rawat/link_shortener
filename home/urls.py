from django.conf.urls import url
from django.urls.conf import path
from home.views import about,home,contact,saveContact,login,signup,shortUrl

urlpatterns = [
    path('', home),
    path('contact/', contact), 
    path('about/', about),
    path('login/', login),
    path('signup/', signup),
    path('short/', shortUrl),
    path('abc/', saveContact),
]