from django.urls import path,include
from web import views


urlpatterns = [
    path("",views.index),
    path("login/",views.loginaction),
    path("signup/",views.signaction),
    path("contactus/",views.contactus),
]
