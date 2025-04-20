from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    UserListCreateView, UserDetailView,
    FriendListView, FriendCreateView,
    AnnouncementListView, AnnouncementCreateView,
    FriendRequestListView, FriendRequestCreateView,
    MessageListView, MessageCreateView,
    FitnessEventListView, FitnessEventUserListView, FitnessEventCreateView, FitnessEventDetailView,
    FitnessChallengeListView, FitnessChallengeUserListView, FitnessChallengeCreateView,
    FlaggedAIMessageListView, FlaggedAIMessageCreateView,
    WorkoutListView, WorkoutCreateView, CustomAuthToken, MessageMarkAsViewedView
)

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('friends/<int:user_id>/', FriendListView.as_view(), name='friend-list'),
    path('announcements/', AnnouncementListView.as_view(), name='announcement-list'),
    path('announcements/create/', AnnouncementCreateView.as_view(), name='announcement-create'),
    path('friend-requests/<int:user_id>/', FriendRequestListView.as_view(), name='friend-request-list'),
    path('messages/<int:user_id>/', MessageListView.as_view(), name='message-list'),
    path('fitness-events/', FitnessEventListView.as_view(), name='fitness-event-list'),
    path('fitness-events/<int:event_id>/', FitnessEventDetailView.as_view(), name='fitness-event-detail'),
    path('fitness-events/user/<int:user_id>/', FitnessEventUserListView.as_view(), name='fitness-event-user-list'),
    path('fitness-events/create/', FitnessEventCreateView.as_view(), name='fitness-event-create'),
    path('fitness-challenges/', FitnessChallengeListView.as_view(), name='fitness-challenge-list'),
    path('fitness-challenges/<int:user_id>/', FitnessChallengeUserListView.as_view(), name='fitness-challenge-user-list'),
    path('fitness-challenges/create/', FitnessChallengeCreateView.as_view(), name='fitness-challenge-create'),
    path('flagged-ai-messages/<int:user_id>/', FlaggedAIMessageListView.as_view(), name='flagged-ai-message-list'),
    path('workouts/<int:user_id>/', WorkoutListView.as_view(), name='workout-list'),
    path('messages/<int:pk>/mark-as-viewed/', MessageMarkAsViewedView.as_view(), name='message-mark-as-viewed'),
]