from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *




class PreviousMessagesView(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        user1 = int(self.kwargs['user1'])
        user2 = int(self.kwargs['user2'])

        thread_suffix = f"{user1}_{user2}" if user1 > user2 else f"{user2}_{user1}"
        thread_name = 'chat_'+thread_suffix
        queryset = Messages.objects.filter(
            thread_name=thread_name
        )
        return queryset
    
