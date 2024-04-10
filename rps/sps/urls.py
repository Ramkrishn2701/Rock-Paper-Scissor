"""
URL configuration for sps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from home import views as home_views

urlpatterns = [
    path('',home_views.index,name='index'),
    path('Players',home_views.Players,name='Player'),
    path('play/<int:value1>/<int:value2>',home_views.play,name='play'),
    path('play',home_views.play,name='play'),
    path('game_data/<int:value1>/<int:value2>',home_views.game_data,name='game_data'),
    path('reset/<int:value1>/<int:value2>',home_views.reset,name='reset'),
    path('admin/', admin.site.urls),
]
