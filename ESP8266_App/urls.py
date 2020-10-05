"""ESP8266_App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from . import views
from ESP8266_Control import views as Control
from ESP8266_Report import views as Report
# app_name = 'ESP8266_App'
urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('admin/', admin.site.urls),
    path('control/', Control.index),
    path('control/<int:device_id>/', Control.index, name='device'),
    path('control/<int:device_id>/<str:command>/', Control.command, name='command'),
    path('control/<int:device_id>/<str:command>/<str:params>/', Control.command_params, name='command_params'),
    path('report/', Report.index),
    path('report/index/', Report.index),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
