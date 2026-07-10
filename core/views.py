from django.shortcuts import render
from rest_framework.views import APIView
from core.models import Chat, Conversation
from core.serializer import *
from rest_framework.response import Response
from services.response import generate_response


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
                  return Response({ 'invalid':'invalid input' })
            
class ChatAPI(APIView):
    def get(self, request):
       data_user=Chat.objects.filter(user=request.user)
       data=Conversation.objects.filter(chat=data_user)
       serial=ConversationSeriailizer(data, many=True)
       return Response(serial.data)
    
    def post(self, request):
        serial=InputSerializer(data=request.data)
        if serial.is_valid():
            input=serial.validated_data['request']
            output=generate_response(input)
            chat_user=Chat.objects.filter(user=request.user)
            Conversation.objects.create(chat=chat_user, chat_request=input, chat_response=output)
            return Response(output)
        else:
             return Response({ 'invalid':'invalid input' })
