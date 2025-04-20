import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Friend(models.Model):
    user_id1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends_as_user1')
    user_id2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends_as_user2')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_id1.email} - {self.user_id2.email}"

class Announcement(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:50]

class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender.email} -> {self.receiver.email}"

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    text = models.TextField()
    viewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender.email} -> {self.receiver.email}: {self.text[:30]}"

class FitnessEvent(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='events_participated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.title
    
class FlaggedAIMessage(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email}: {self.text[:30]}"

class Workout(models.Model):
    WORKOUT_TYPES = [
        ('cardio', 'Cardio'),
        ('muscle', 'Muscle'),
        ('flexibility', 'Flexibility'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=WORKOUT_TYPES)
    tp = models.CharField(max_length=255)
    start_time = models.DateTimeField()  
    end_time = models.DateTimeField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email}: {self.type} - {self.description[:30]}"

class FitnessChallenge(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='challenges_participated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    workouts = models.ManyToManyField(Workout, related_name='challenges', blank=True)
    def __str__(self):
        return self.title
