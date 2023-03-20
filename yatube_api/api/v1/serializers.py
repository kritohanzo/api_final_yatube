from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from posts.models import Comment, Follow, Group, Post


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = ("id", "text", "pub_date", "author", "image", "group")
        model = Post
        read_only_fields = ("author",)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        fields = ("id", "author", "post", "text", "created")
        model = Comment
        read_only_fields = ("author", "post")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "title", "slug", "description")
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)
    following = serializers.CharField()

    class Meta:
        fields = ("user", "following")
        model = Follow
        read_only_fields = ("user",)

    def validate_following(self, value):
        user = self.context.get("request").user
        value = get_object_or_404(User, username=value)
        if user == value:
            raise serializers.ValidationError("Unable to subscribe to myself")
        if Follow.objects.filter(user=user, following=value).exists():
            raise serializers.ValidationError(
                "Following to this user already exist"
            )
        return value
