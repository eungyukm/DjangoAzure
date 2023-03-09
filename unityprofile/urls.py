from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('galaxy10profiledatatable', views.galaxys10profiledatatable),
    path('galaxy9profiledatatable', views.galaxys9profiledatatable),
    path('galaxy8profiledatatable', views.galaxys8profiledatatable),
    path('iphone11profiledatatable', views.iphone11profiledatatable),
    path('remove_profiledatatable', views.remove_profiledatatable),
]
