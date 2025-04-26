from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Friend, Announcement, FriendRequest, Message, FitnessEvent, FitnessChallenge, FlaggedAIMessage, Workout, UserWorkout
from .serializers import (
    UserSerializer, FriendSerializer, AnnouncementSerializer, FriendRequestSerializer,
    MessageSerializer, FitnessEventSerializer, FitnessChallengeSerializer,
    FlaggedAIMessageSerializer, WorkoutSerializer, UserWorkoutSerializer
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
import requests
from django.conf import settings
from django.shortcuts import redirect
from django.http import JsonResponse

    
class BatchUserLookupView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user_ids = self.request.query_params.get('ids', '').split(',')
        
        if not user_ids or not user_ids[0]:  
            return User.objects.none()
        try:
            user_ids = [int(id) for id in user_ids]
            return User.objects.filter(id__in=user_ids)
        except ValueError:
            return User.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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
    permission_classes = [AllowAny]

class FriendListView(generics.ListAPIView):
    serializer_class = FriendSerializer
    permission_classes = [AllowAny]
    
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
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return FriendRequest.objects.filter(receiver=user_id)

class FriendRequestCreateView(generics.CreateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer


class MessageReceivedListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Message.objects.filter(receiver=user_id)

class MessageSentListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Message.objects.filter(sender=user_id)

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
    
class BatchWorkoutLookupView(generics.ListAPIView):
    serializer_class = WorkoutSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        workout_ids = self.request.query_params.get('ids', '').split(',')
        
        if not workout_ids or not workout_ids[0]:  
            return Workout.objects.none()
        try:
            workout_ids = [int(id) for id in workout_ids]
            return Workout.objects.filter(id__in=workout_ids)
        except ValueError:
            return Workout.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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

class UserWorkoutListView(generics.ListAPIView):
    serializer_class = UserWorkoutSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return UserWorkout.objects.filter(user=user_id)
    
class UserWorkoutCreateView(generics.CreateAPIView):
    queryset = UserWorkout.objects.all()
    serializer_class = UserWorkoutSerializer
    permission_classes = [AllowAny]

class WorkoutCompletionsListView(generics.ListAPIView):
    """Get all users who completed a specific workout"""
    serializer_class = UserWorkoutSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        workout_id = self.kwargs['workout_id']
        return UserWorkout.objects.filter(workout=workout_id)


STRAVA_CLIENT_ID = '156568'
STRAVA_CLIENT_SECRET = settings.STRAVA_CLIENT_SECRET  # pull from env or settings.py
REDIRECT_URI = 'http://127.0.0.1:8000/api/strava/callback/'  # Make sure it matches Strava config


def strava_login(request):
    auth_url = (
        f"https://www.strava.com/oauth/authorize"
        f"?client_id={STRAVA_CLIENT_ID}"
        f"&response_type=code"
        f"&redirect_uri={REDIRECT_URI}"
        f"&approval_prompt=auto"
        f"&scope=read,activity:read"
    )
    return redirect(auth_url)


def strava_callback(request):
    code = request.GET.get('code')

    token_response = requests.post(
        'https://www.strava.com/oauth/token',
        data={
            'client_id': '156568',
            'client_secret': 'fd86fc31b5880bdce098b94e0a2bc703819693ed',
            'code': code,
            'grant_type': 'authorization_code'
        }
    )

    token_data = token_response.json()
    access_token = token_data.get('access_token')

    # Make test API call
    if access_token:
        headers = {'Authorization': f'Bearer {access_token}'}
        activities_response = requests.get('https://www.strava.com/api/v3/athlete/activities', headers=headers)

        if activities_response.status_code == 200:
            activities = activities_response.json()
            print("Strava Activities:")
            for activity in activities[:5]:  # Limit to first 5
                print(f"Name: {activity['name']} | Distance: {activity['distance']}m")
        else:
            print("Failed to fetch activities:", activities_response.text)
    else:
        print("No access token returned:", token_data)

    return JsonResponse(token_data)
