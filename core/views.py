from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from core.models import Chat, Conversation
from core.serializer import *
from rest_framework.response import Response
from services.response import generate_response
from rest_framework.permissions import IsAuthenticated


class RegisterAPI(APIView):
    def post(self, request):
            serial=RegisterSerializer(data=request.data)
            if serial.is_valid():
                  first_name=serial.validated_data['first_name']
                  last_name=serial.validated_data['last_name']
                  username=serial.validated_data['username']
                  email=serial.validated_data['email']
                  password=serial.validated_data['password']

                  if User.objects.filter(username=username).exists():
                        return Response({ 'message':'user already exists' })
                  else:
                        User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                        return Response({ 'message':'Registration successfull' })
            else:
                  return Response(serial.errors, status=400)
            
class ChatAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        data=Chat.objects.filter(user=request.user)
        serial=ChatSerializer(data, many=True)
        return Response(serial.data)
    def post(self, request):
        serial=ChatSerializer(data=request.data)
        if serial.is_valid():
            serial.save(user=request.user)
            return Response(serial.data)
        else:
            return Response({ 'invalid':'invalid inputs' })

class ConversationAPI(APIView):
    def get(self, request, pk):
        data=get_object_or_404(Chat, id=pk)
        convo=Conversation.objects.filter(chat=data)
        serial=ConversationSeriailizer(convo, many=True)
        return Response(serial.data)

    def post(self, request, pk):
        serial=InputSerializer(data=request.data)
        if serial.is_valid():
            input=serial.validated_data['chat_request']
            output=generate_response(input)
            chat_user, _ = Chat.objects.get_or_create(user=request.user)
            Conversation.objects.create(chat=chat_user, chat_request=input, chat_response=output)
            return Response(output)
        else:
             return Response(serial.errors, status=400)
