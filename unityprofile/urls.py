from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('galaxy10profiledatatable', views.galaxys10profiledatatable),
    path('galaxy9profiledatatable', views.galaxys9profiledatatable),
    path('galaxy8profiledatatable', views.galaxys8profiledatatable),
    path('iphone11profiledatatable', views.iphone11profiledatatable),
    path('remove_profiledatatable', views.remove_profiledatatable),

    # 테스트 시나리오 저장
    path('write_scenario', views.write_scenario),
    path('scenario_write_result', views.scenario_write_result),
    path('scenario_main', views.scenario_main),
    path('scenario_modify', views.scenario_modify),
    path('scenario_modify_result', views.scenario_write_result),

    # 테스트 iphone11test
    path('iphone11test', views.iphone11test),
]
