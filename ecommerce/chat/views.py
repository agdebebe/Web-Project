from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

from .models import Chat

# /***************************************************************************************
# # *    Title: <twillo>
# # *    Author: <Kevin Ndung'u>
# # *    Date: <19 August 2013>
# # *    Code version: <python>
# # *    Availability: <https://www.twilio.com/blog/2018/05/build-chat-python-django-applications-programmable-chat.html>
# # *   Edited by:
# # ***************************************************************************************/
def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

def chat_view(requets):
	return render(requets,'chat/chat.html',{})
