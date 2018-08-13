from django.conf.urls import url, include
from rest_framework import routers
from Bookmarks.AppBookmarks import views

router_app_bookmarks = routers.DefaultRouter()
router_app_bookmarks.register(r'users', views.UserViewSet)
router_app_bookmarks.register(r'bookmarks', views.BookmarksViewSet)

