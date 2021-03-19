from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.basepage,name='basepage'),
    path('eventspage/',views.eventspage,name='eventspage'),
    path('teams/',views.teampage,name='teampage'),
    path('about/',views.aboutuspage,name='aboutuspage'),
    ]
