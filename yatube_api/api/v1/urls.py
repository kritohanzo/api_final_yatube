from rest_framework import routers

from django.urls import include, path

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


router_v1 = routers.DefaultRouter()
router_v1.register(r"posts", PostViewSet)
router_v1.register(
    r"posts/(?P<post_id>\d+)/comments",
    CommentViewSet,
    basename="post-comments",
)
router_v1.register(r"groups", GroupViewSet)
router_v1.register(r"follow", FollowViewSet, basename="user-follows")

urlpatterns = [
    path("", include(router_v1.urls)),
    path("", include("djoser.urls")),
    path("", include("djoser.urls.jwt")),
]
