from django.urls import path
from .views import (
    UserListCreateView,
    FriendListView,
    AnnouncementListCreateView,
    FriendRequestListView,
    MessageListView,
    FitnessEventListCreateView,
    FitnessEventUserListView,
    FitnessChallengeListCreateView,
    FitnessChallengeUserListView,
    FlaggedAIMessageListView,
    WorkoutListView
)

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('friends/<int:user_id>/', FriendListView.as_view(), name='friend-list'),
    path('announcements/', AnnouncementListCreateView.as_view(), name='announcement-list'),
    path('announcements/create/', AnnouncementListCreateView.as_view(), name='announcement-create'),
    path('friend-requests/<int:user_id>/', FriendRequestListView.as_view(), name='friend-request-list'),
    path('messages/<int:user_id>/', MessageListView.as_view(), name='message-list'),
    path('fitness-events/', FitnessEventListCreateView.as_view(), name='fitness-event-list'),
    path('fitness-events/<int:user_id>/', FitnessEventUserListView.as_view(), name='fitness-event-user-list'),
    path('fitness-events/create/', FitnessEventListCreateView.as_view(), name='fitness-event-create'),
    path('fitness-challenges/', FitnessChallengeListCreateView.as_view(), name='fitness-challenge-list'),
    path('fitness-challenges/<int:user_id>/', FitnessChallengeUserListView.as_view(), name='fitness-challenge-user-list'),
    path('fitness-challenges/create/', FitnessChallengeListCreateView.as_view(), name='fitness-challenge-create'),
    path('flagged-ai-messages/<int:user_id>/', FlaggedAIMessageListView.as_view(), name='flagged-ai-message-list'),
    path('workouts/<int:user_id>/', WorkoutListView.as_view(), name='workout-list'),
]