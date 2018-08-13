

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, BookmarkSerializer







class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class BookmarksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bookmarks to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = BookmarkSerializer