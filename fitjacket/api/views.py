from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Friend, Announcement, FriendRequest, Message, FitnessEvent, FitnessChallenge, FlaggedAIMessage, Workout
from .serializers import (
    UserSerializer, FriendSerializer, AnnouncementSerializer, FriendRequestSerializer,
    MessageSerializer, FitnessEventSerializer, FitnessChallengeSerializer,
    FlaggedAIMessageSerializer, WorkoutSerializer
)

# Create your views here.

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FriendListView(generics.ListAPIView):
    serializer_class = FriendSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Friend.objects.filter(user_id1=user_id) | Friend.objects.filter(user_id2=user_id)

class FriendCreateView(generics.CreateAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class AnnouncementListView(generics.ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class AnnouncementCreateView(generics.CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class FriendRequestListView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return FriendRequest.objects.filter(receiver=user_id)

class FriendRequestCreateView(generics.CreateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer


class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Message.objects.filter(receiver=user_id)

class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class FitnessEventListView(generics.ListAPIView):
    queryset = FitnessEvent.objects.all()
    serializer_class = FitnessEventSerializer

class FitnessEventUserListView(generics.ListAPIView):
    serializer_class = FitnessEventSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return FitnessEvent.objects.filter(user=user_id) | FitnessEvent.objects.filter(participants=user_id)

class FitnessEventCreateView(generics.CreateAPIView):
    queryset = FitnessEvent.objects.all()
    serializer_class = FitnessEventSerializer

class FitnessChallengeListView(generics.ListAPIView):
    queryset = FitnessChallenge.objects.all()
    serializer_class = FitnessChallengeSerializer

class FitnessChallengeUserListView(generics.ListAPIView):
    serializer_class = FitnessChallengeSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return FitnessChallenge.objects.filter(user=user_id) | FitnessChallenge.objects.filter(participants=user_id)

class FitnessChallengeCreateView(generics.CreateAPIView):
    queryset = FitnessChallenge.objects.all()
    serializer_class = FitnessChallengeSerializer

class FlaggedAIMessageListView(generics.ListAPIView):
    serializer_class = FlaggedAIMessageSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return FlaggedAIMessage.objects.filter(user=user_id)

class FlaggedAIMessageCreateView(generics.CreateAPIView):
    queryset = FlaggedAIMessage.objects.all()
    serializer_class = FlaggedAIMessageSerializer

class WorkoutListView(generics.ListAPIView):
    serializer_class = WorkoutSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Workout.objects.filter(user=user_id)

class WorkoutCreateView(generics.CreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
