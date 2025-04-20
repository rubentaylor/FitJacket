from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Friend, Announcement, FriendRequest, Message, FitnessEvent, FitnessChallenge, FlaggedAIMessage, Workout
from .serializers import (
    UserSerializer, FriendSerializer, AnnouncementSerializer, FriendRequestSerializer,
    MessageSerializer, FitnessEventSerializer, FitnessChallengeSerializer,
    FlaggedAIMessageSerializer, WorkoutSerializer
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

# Create your views here.

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        user = serializer.instance
        token, created = Token.objects.get_or_create(user=user)
        
        response_data = serializer.data
        response_data['token'] = token.key
        
        headers = self.get_success_headers(serializer.data)
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

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
    permission_classes = [AllowAny]

class FitnessEventDetailView(generics.RetrieveAPIView):
    queryset = FitnessEvent.objects.all()
    serializer_class = FitnessEventSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'event_id'
    permission_classes = [AllowAny]

class FitnessEventUserListView(generics.ListAPIView):
    serializer_class = FitnessEventSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return FitnessEvent.objects.filter(user=user_id) | FitnessEvent.objects.filter(participants=user_id)

class FitnessEventCreateView(generics.CreateAPIView):
    queryset = FitnessEvent.objects.all()
    serializer_class = FitnessEventSerializer
    permission_classes = [AllowAny]

class FitnessChallengeListView(generics.ListAPIView):
    queryset = FitnessChallenge.objects.all()
    serializer_class = FitnessChallengeSerializer
    permission_classes = [AllowAny]

class FitnessChallengeUserListView(generics.ListAPIView):
    serializer_class = FitnessChallengeSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return FitnessChallenge.objects.filter(user=user_id) | FitnessChallenge.objects.filter(participants=user_id)

class FitnessChallengeCreateView(generics.CreateAPIView):
    queryset = FitnessChallenge.objects.all()
    serializer_class = FitnessChallengeSerializer
    permission_classes = [AllowAny]

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

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                         context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username
        })
    
class MessageMarkAsViewedView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    def update(self, request, *args, **kwargs):
        message = self.get_object()
        message.viewed = True
        message.save()
        return Response(self.get_serializer(message).data)