from rest_framework.generics import ListAPIView,CreateAPIView

from .serializers import ChatSerializer
from chat.models import Chat

class ChatListAPIView(ListAPIView):
	queryset = Chat.objects.all()
	serializer_class = ChatSerializer

class ChatAddAPIView(CreateAPIView):
	queryset = Chat.objects.all()
	serializer_class = ChatSerializer

