from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='indxe'),
    path('about', views.about, name='about'),
]
