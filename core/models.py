from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name

class Conversation(models.Model):
    chat=models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='convo')
    chat_request=models.TextField()
    chat_response=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chat_request[:100]

