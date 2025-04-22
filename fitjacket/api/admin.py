from django.contrib import admin
from .models import (
    Friend, Announcement, FriendRequest, Message,
    FitnessEvent, FitnessChallenge, FlaggedAIMessage, Workout
)


# Register your models here.
@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id1', 'user_id2', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user_id1__username', 'user_id2__username')

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('text',)

@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('sender__username', 'receiver__username')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'viewed', 'created_at', 'updated_at')
    list_filter = ('viewed', 'created_at', 'updated_at')
    search_fields = ('sender__username', 'receiver__username', 'text')

@admin.register(FitnessEvent)
class FitnessEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'start_time', 'end_time', 'location', 'created_at', 'updated_at')
    list_filter = ('start_time', 'end_time', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'user__username', 'location')
    filter_horizontal = ('participants',)

@admin.register(FitnessChallenge)
class FitnessChallengeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'start_time', 'end_time', 'created_at', 'updated_at')
    list_filter = ('start_time', 'end_time', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'user__username')
    filter_horizontal = ('participants', 'workouts',)

@admin.register(FlaggedAIMessage)
class FlaggedAIMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__username', 'text')

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'type', 'start_time', 'end_time', 'created_at', 'updated_at')
    list_filter = ('type', 'start_time', 'end_time', 'created_at', 'updated_at')
    search_fields = ('user__username', 'description', 'type')