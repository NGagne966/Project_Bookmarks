from django.contrib.auth.models import User
from rest_framework import serializers

from Bookmarks.AppBookmarks.models import Bookmark

# TEST pull up
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Bookmark
        fields = ('id', 'title', 'site_link', 'type', 'description', 'created', 'last_check', )
