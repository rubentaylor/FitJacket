from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import (
    Friend, Announcement, FriendRequest, Message,
    FitnessEvent, FitnessChallenge, FlaggedAIMessage, Workout
)


class UserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'token']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        token = Token.objects.create(user=user)
        validated_data['token'] = token.key
        return user

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ['id', 'user_id1', 'user_id2', 'created_at', 'updated_at']

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'text', 'created_at', 'updated_at']

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['id', 'sender', 'receiver', 'created_at', 'updated_at']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'text','viewed','created_at', 'updated_at']

class FitnessEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessEvent
        fields = ['id', 'start_time', 'end_time', 'description', 'title', 'user', 'participants', 'location', 'created_at', 'updated_at']

class FitnessChallengeSerializer(serializers.ModelSerializer):
    workouts = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Workout.objects.all(),
        required=False
    )
    class Meta:
        model = FitnessChallenge
        fields = ['id', 'start_time', 'end_time', 'description', 'title', 'user', 'participants', 'workouts', 'created_at', 'updated_at']

class FlaggedAIMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlaggedAIMessage
        fields = ['id', 'text', 'user', 'created_at', 'updated_at']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'user', 'description', 'type', 'tp', 'start_time', 'end_time', 'created_at', 'updated_at']