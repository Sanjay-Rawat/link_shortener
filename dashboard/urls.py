from django.conf.urls import url
from dashboard import views


urlpatterns = [
    # url('', views.dashboard), # for method
    url('dash/', views.HomePageView.as_view()), # for class
    url('dashboard/', views.dashboard), # for method
]