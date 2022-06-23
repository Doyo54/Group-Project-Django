from django.urls import re_path,include
from . import views
from doyo.views import index


urlpatterns = [
    re_path(r'', views.home, name='home'),
]