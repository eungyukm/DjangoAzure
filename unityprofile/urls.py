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
    path('scenario_modify_result', views.scenario_modify_result),

    # 전체 프로파일 데이터 출력
    path('profiledata_all', views.profiledata_all),


    # 프로젝트 별 시나리오를 관리
    path('project_scenario_main', views.project_scenario_main),
    path('project_scenario_modify', views.project_scenario_modify),
    path('project_scenario_modify_result', views.project_scenario_modify_result),
    path('project_scenario_delete', views.project_scenario_delete),

    # 시나리오 별 프로파일 결과 관리
    path('profile_result_main', views.profile_result_main),
]
