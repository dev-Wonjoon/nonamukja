from django.db import models
from core.models import TimeStampedModel
from accounts.models import User

class Post(TimeStampedModel):
    
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    
