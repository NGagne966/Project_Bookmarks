from django.contrib.auth.models import User
from rest_framework import serializers

from Bookmarks.AppBookmarks.models import Bookmark

# TEST pull up
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff',)


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Bookmark
        fields = ('id', 'url', 'title', 'site_link', 'type', 'description', 'created', 'last_check', )
