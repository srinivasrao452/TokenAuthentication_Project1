"""TokenAuthentication_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url,include
from rest_framework.authtoken import views

from TokenAuthentication_App import views as myviews

urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'api/' , include('TokenAuthentication_App.urls')),
    url(r'gettoken/$',views.obtain_auth_token),

    url(r'auth/', myviews.login_form),
    url(r'loginuser/' , myviews.login_user),


]



