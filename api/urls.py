from django.urls import path
from . import views

urlpatterns = [
    path('GET', views.getData),
    path('POST', views.postData),

    # 로그인
    path('login', views.api_login_view),
    # 로그인 확인
    path('login_result', views.api_login_result),
]
