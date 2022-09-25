from rest_framework import viewsets

from .serializers import UserSerializer, ClubSerializer, ThreadSerializer, CommentSerializer
from .models import User, Club, Thread, Comment


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClubViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class ThreadViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
