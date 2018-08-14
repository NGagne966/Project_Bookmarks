

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .serializers import UserSerializer, BookmarkSerializer







class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class BookmarksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bookmarks to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = BookmarkSerializer