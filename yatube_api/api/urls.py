from django.urls import path, include
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('', include('djoser.urls.jwt')),
]
