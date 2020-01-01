from rest_framework import serializers
from django.utils.timesince import timesince
from chat.models import Chat

class ChatSerializer(serializers.ModelSerializer):
	username = serializers.SerializerMethodField()
	timesince = serializers.SerializerMethodField()
	class Meta:
		model = Chat
		fields = '__all__'

	def get_username(self,obj):
		return obj.user.username

	def get_timesince(self,obj):
		return timesince(obj.timestamp)