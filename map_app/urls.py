from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('map_main', views.map_main, name='map_main'),
    path('map_modify', views.map_modify, name='map_modify'),
    path('map_write', views.map_write, name='map_write'),
    path('map_read', views.map_read, name='map_read'),
    path('map_write_result', views.map_write_result, name='map_write_result'),
    path('map_modify_result', views.map_modify_result, name='map_modify_result'),
    path('map_delete', views.map_delete, name='map_delete'),
]
