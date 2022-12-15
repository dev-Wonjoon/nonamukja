from django.contrib.auth import get_user_model
from django.db import models
from accounts.models import User
from core.models import TimeStampedModel

User = get_user_model()


class ChatRoom(TimeStampedModel):
    name = models.CharField(max_length=255)

    

class Message(models.Model):
    user_id = models.ForeignKey(User, related_name='user_message', on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, related_name='room_id', on_delete=models.CASCADE) 
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_message(self):
        return Message.objects.order_by('-timestamp').all()[:10]
