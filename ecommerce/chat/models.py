from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# /***************************************************************************************
# *    Title: <Chat tutorial>
# *    Author: <9cv9 official>
# *    Date: <21 september 2018>
# *    Code version: <python>
# *    Availability: <https://medium.com/@9cv9official/simple-chat-app-using-django-channel-ed5032b79b9c/>
# *   Edited by:
# ***************************************************************************************/ -->
class Chat(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	message = models.TextField()

	def __str__(self):
		return self.user.email
