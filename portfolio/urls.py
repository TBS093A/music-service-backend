"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions
from rest_framework.authtoken import views as authViews

from portfolio import settings
from .account import views

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='0.1',
      description="API",
      contact=openapi.Contact(email="zukkamil.44@gmail.com"),
      license=openapi.License(name="All rights reserved"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register(r'users', views.AccountViewSet, basename='user')
# router.register(r'users/auth', views.AccountAuth, basename='user auth')
router.register(r'guests', views.GuestViewSet)

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include(router.urls)),
        # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]

if settings.DEBUG:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include(router.urls)),
        re_path(r'users/auth', views.AccountAuth.as_view()),
        # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0))
    ]