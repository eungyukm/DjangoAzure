"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relecloud.urls')),
    # 사용자 관련
    path('user/', include('user_app.urls')),
    # 게시판 관련
    path('board/', include('board_app.urls')),
    # 맵 관련
    path('map/', include('map_app.urls')),
    # 사용자 관련 Rest API
    path('api/account/', include('api.urls')),
    path('api/', include('api.urls')),
    # 프로파일 관련
    path('profile/', include('unityprofile.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
