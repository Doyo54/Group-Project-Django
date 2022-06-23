from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('searchresults', views.searchresults, name='searchresults'),
    path('profile', views.profile, name='profile')
]