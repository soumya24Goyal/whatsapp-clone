"""api URL Configuration

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
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.urls import path
from uapp import views

app_name='api'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view()),
    path('add/',views.PostUser.as_view()),
    path('getuser/',views.GETUser.as_view()),
    path('update/',views.PUTUser.as_view()),
    path('deleteuser/',views.DeleteUser.as_view()),
    path('otpg/',views.OTPGenerate.as_view()),
    path('otpv/',views.validateOtp.as_view()),
    path('create/',views.Chatapp.as_view()),
]

