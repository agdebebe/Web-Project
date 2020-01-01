from .views import ChatListAPIView
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('chat/list/',ChatListAPIView.as_view(),name='list')
]
