from django.urls import path
from . import views

urlpatterns = [
    path('GET', views.getData),
    path('POST', views.postData),

    # 로그인
    path('login', views.api_login_view),
    # 로그인 확인
    path('login_result', views.api_login_result),

    # 맵 등록
    path('map_create', views.api_map_create),

    # 맵 조회
    path('map_select', views.api_map_select),

    # 프로 파일 데이터 저장
    path('profile', views.api_profile_result),

    # 경고 프로파일 데이터
    path('warning_profile', views.api_warning_profile_result),
]
