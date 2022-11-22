from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
]

#file >> function express
#path(takes 3 parameters) 
#first parameter ---> route name
#second parameter ----> ဘယ် file ထဲက ဘယ်functionဆိုတာ ---> views.py --> home function
#third parameter ----> name