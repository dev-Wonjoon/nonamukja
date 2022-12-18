from django.contrib.auth import get_user_model
from django.db import models
from accounts.models import User
from core.models import TimeStampedModel

User = get_user_model()

class Room(TimeStampedModel):
    class Meta:
        db_table = "room"

class RoomJoin(TimeStampedModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roomJoin")
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="roomJoin")

    class Meta:
        db_table = "roomJoin"
    

class Message(TimeStampedModel):
    message = models.CharField(max_length=500)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message")
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="message")

    class Meta:
        db_table = "message"

    def __str__(self):
        return self.user_id.email

    def last_30_message(self, room_id):
        return Message.objects.filter(room_id=room_id).order_by('created_at')[:30]
