from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('sayHello', views.sayHello, name='sayHello'),
    path('api-token-auth/', obtain_auth_token)
]