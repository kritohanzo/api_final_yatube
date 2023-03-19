from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post, Group, Follow

from django.contrib.auth.models import User



class UserID2Username(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return User.objects.all()

    def to_internal_value(self, data):
        try:
            user = User.objects.get(username=data)
            return user
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this username does not exist")
        
class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')
        model = Post
        read_only_fields = ('author',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
        read_only_fields = ('author', 'post')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group

class FollowSerializer(serializers.ModelSerializer):
    following = UserID2Username()

    class Meta:
        fields = ('user', 'following')
        model = Follow
        read_only_fields = ('user',)
