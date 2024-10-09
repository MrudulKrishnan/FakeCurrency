from django.contrib import admin
from django.urls import path

from AccountApp.views import *


urlpatterns = [
    path('', HomePage.as_view(), name="home_page"),
    path('login_page/', LoginPage.as_view(), name="login_page")

   
]
