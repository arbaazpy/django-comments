from rest_framework import routers

from .viewsets import UserViewSet, ClubViewSet, ThreadViewSet, CommentViewSet
from .viewsets2 import CommentViewSet as CommentViewSet2

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'clubs', ClubViewSet)
router.register(r'threads', ThreadViewSet)
router.register(r'comments', CommentViewSet)

router.register(r'v2/comments', CommentViewSet2)

