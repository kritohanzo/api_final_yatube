from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from django.contrib.auth.models import User

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
    following = serializers.CharField(source="following.username")
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        fields = ("user", "following")
        model = Follow
        read_only_fields = ("user",)

    def create(self, validated_data):
        following_username = validated_data.pop("following").get("username")
        if following_username == validated_data.get("user").username:
            raise serializers.ValidationError(
                {"following": "Unable to subscribe to myself"}
            )
        if Follow.objects.filter(
            user=validated_data.get("user"),
            following__username=following_username,
        ).exists():
            raise serializers.ValidationError(
                {"following": "Following to this user already exist"}
            )
        try:
            following_user = User.objects.get(username=following_username)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"following": "User with this username does not exist"}
            )
        validated_data["following"] = following_user
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
