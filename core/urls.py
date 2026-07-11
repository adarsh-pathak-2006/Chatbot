from django.urls import path
from core.views import ChatAPI, ConversationAPI

urlpatterns = [
    path('chat/', ChatAPI.as_view(), name='chat'),
    path('chat/<int:pk>/', ConversationAPI.as_view(), name='converation individual')
]
