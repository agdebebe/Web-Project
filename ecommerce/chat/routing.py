from django.urls import re_path

from . import consumers

# /***************************************************************************************
# *    Title: <Chat tutorial>
# *    Author: <9cv9 official>
# *    Date: <21 september 2018>
# *    Code version: <python>
# *    Availability: <https://medium.com/@9cv9official/simple-chat-app-using-django-channel-ed5032b79b9c/>
# *   Edited by: 
# ***************************************************************************************/ -->
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]
