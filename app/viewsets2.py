from rest_framework import viewsets

from .serializers import CommentSerializer
from .models import Comment


class CommentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Comment.objects.select_related("user", "thread__creator").all()
    serializer_class = CommentSerializer
