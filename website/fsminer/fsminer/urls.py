"""fsminer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from website.views import website, get_miner_pool_api, get_latest_version
from serialcode.views import activate_code
from users.views import userinfo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('website/', website, name='website'),
    path('activate/', activate_code, name='activate'),
    path('get_miner_pool/', get_miner_pool_api, name='get_miner_pool'),
    path('userinfo/', userinfo, name='userinfo'),
    path('get_latest_version/', get_latest_version, name='userinfo'),
]
