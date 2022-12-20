from rest_framework import serializer
from .models import Message, Room, RoomJoin

class MessageSerializer(serializers.ModelSerialzier):
    class Meta:
        model = Message
        fields = ['message', 'user_id', 'created-at']

