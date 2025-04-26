from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from .views import (
    UserListCreateView, UserDetailView,
    FriendListView, FriendCreateView,
    AnnouncementListView, AnnouncementCreateView,
    FriendRequestListView, FriendRequestCreateView,
    MessageReceivedListView, MessageSentListView, MessageCreateView,
    FitnessEventListView, FitnessEventUserListView, FitnessEventCreateView, FitnessEventDetailView,
    FitnessChallengeListView, FitnessChallengeUserListView, FitnessChallengeCreateView,
    FlaggedAIMessageListView,
    WorkoutListView, CustomAuthToken, MessageMarkAsViewedView, BatchUserLookupView, BatchWorkoutLookupView
)

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('friends/<int:user_id>/', FriendListView.as_view(), name='friend-list'),
    path('announcements/', AnnouncementListView.as_view(), name='announcement-list'),
    path('announcements/create/', AnnouncementCreateView.as_view(), name='announcement-create'),
    path('friend-requests/<int:user_id>/', FriendRequestListView.as_view(), name='friend-request-list'),
    path('messages/received/<int:user_id>/', MessageReceivedListView.as_view(), name='message-received-list'),
    path('messages/sent/<int:user_id>/', MessageSentListView.as_view(), name='message-sent-list'),
    path('fitness-events/', FitnessEventListView.as_view(), name='fitness-event-list'),
    path('fitness-events/<int:event_id>/', FitnessEventDetailView.as_view(), name='fitness-event-detail'),
    path('fitness-events/user/<int:user_id>/', FitnessEventUserListView.as_view(), name='fitness-event-user-list'),
    path('fitness-events/create/', FitnessEventCreateView.as_view(), name='fitness-event-create'),
    path('fitness-challenges/', FitnessChallengeListView.as_view(), name='fitness-challenge-list'),
    path('fitness-challenges/user/<int:user_id>/', FitnessChallengeUserListView.as_view(), name='fitness-challenge-user-list'),
    path('fitness-challenges/create/', FitnessChallengeCreateView.as_view(), name='fitness-challenge-create'),
    path('flagged-ai-messages/<int:user_id>/', FlaggedAIMessageListView.as_view(), name='flagged-ai-message-list'),
    path('workouts/<int:user_id>/', WorkoutListView.as_view(), name='workout-list'),
    path('workouts/batch/', BatchWorkoutLookupView.as_view(), name='batch-workout-lookup'),
    path('messages/<int:pk>/mark-as-viewed/', MessageMarkAsViewedView.as_view(), name='message-mark-as-viewed'),
    path('users/batch/', BatchUserLookupView.as_view(), name='batch-user-lookup'),
    path('strava/login/', views.strava_login, name='strava_login'),
    path('strava/callback/', views.strava_callback, name='strava_callback'),
]