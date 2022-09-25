from rest_framework import serializers

from .models import User, Club, Thread, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source="user.name")
    username = serializers.SerializerMethodField()
    thread_creator = serializers.CharField(source="thread.creator.name")
    # thread_creator = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"

    def get_username(self, obj):
        return obj.user.name

    # def get_thread_creator(self, obj):
    #     return obj.thread.creator.name