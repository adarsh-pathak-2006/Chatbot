from rest_framework.serializers import ModelSerializer
from core.models import Chat, Conversation
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email']

class RegisterSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'password']

class ChatSerializer(ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Chat
        fields='__all__'

class ConversationSeriailizer(ModelSerializer):
    chat=ChatSerializer(read_only=True)
    class Meta:
        model=Conversation
        fields='__all__'

class InputSerializer(ModelSerializer):
    class Meta:
        model=Conversation
        fields=['request']