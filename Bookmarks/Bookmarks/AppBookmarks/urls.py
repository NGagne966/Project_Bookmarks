
from rest_framework import routers
from Bookmarks.AppBookmarks import views


router_app_bookmarks = routers.DefaultRouter()
router_app_bookmarks.register(r'users', views.UserViewSet)
router_app_bookmarks.register(r'bookmarks', views.BookmarksViewSet)
router_app_bookmarks.register(r'new_bookmarks', views.CreateBookmarkViewSet, base_name='new_bookmarks')
# I made some change

url_app_bookmarks = [

]

url_app_bookmarks += router_app_bookmarks.urls