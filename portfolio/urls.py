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
from account.views import GuestViewSet, AccountViewSet, AccountAuth
from album.views import AlbumViewSet, TrackViewSet, TrackRowViewSet
from rating.views import TrackRatingViewSet, AlbumRatingViewSet, CommentRatingViewSet
from comment.views import UserCommentViewSet, GuestCommentViewSet

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
router.register(r'user', AccountViewSet, basename='user')
router.register(r'guest', GuestViewSet, basename='guest')

router.register(r'album', AlbumViewSet, basename='album')
router.register(r'track', TrackViewSet, basename='track')
router.register(r'track-row', TrackRowViewSet, basename='track row')

router.register(r'track/(?P<track_id>\w+)/rating', TrackRatingViewSet, basename='track rating')
router.register(r'album/(?P<album_id>\w+)/rating', AlbumRatingViewSet, basename='album rating')
router.register(r'comment/(?P<comment_id>\w+)/rating', CommentRatingViewSet, basename='comment rating')

router.register(r'comment/user', UserCommentViewSet, basename='user-comment')
router.register(r'comment/guest', GuestCommentViewSet, basename='guest-comment')

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include(router.urls)),
        re_path(r'user/auth', AccountAuth.as_view())
    ]

if settings.DEBUG:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include(router.urls)),
        re_path(r'user/auth', AccountAuth.as_view()),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0))
    ]