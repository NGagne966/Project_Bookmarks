

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .serializers import UserSerializer, BookmarkSerializer
from Bookmarks.AppBookmarks.models import Bookmark



from rest_framework import mixins





class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class BookmarksViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows bookmarks to be viewed
    """
    queryset = Bookmark.objects.all().order_by('-created')
    serializer_class = BookmarkSerializer


class CreateBookmarkViewSet(mixins.CreateModelMixin,
                                viewsets.GenericViewSet):
    """
    A viewset that provides `create`, actions.
    """
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer