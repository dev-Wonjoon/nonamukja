from django.contrib.auth import get_user_model
from django.db import models
from accounts.models import User
from core.models import TimeStampedModel

User = get_user_model()

class Room(TimeStampedModel):
    title = models.CharField(max_length=127)

class RoomJoin(TimeStampedModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roonJoin") 
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="roomJoin")

class Message(TimeStampedModel):
    message = models.CharField(max_length=500)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message")
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="message")
