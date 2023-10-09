from chat.views.chat import (
    ChatAPIView,
    DeleteSavedChatApiView,
    MyChatsApiView,
    SavedChatApiView,
    UpdateDeleteChatApiView,
)
from chat.views.message import MessagesApiView, UpdateDeleteMessageApiView
from django.urls import path

urlpatterns = [
    path("chat/saved_chats/", SavedChatApiView.as_view(), name="get_saved_chats"),
    path("chat/my_chats/", MyChatsApiView.as_view(), name="my_chats"),
    path("chat/<int:pk>/", UpdateDeleteChatApiView.as_view(), name="update_delete_chat"),
    path("chat/<str:room_name>/", ChatAPIView.as_view(), name="get_post_chats"),
    path("chat/<int:chat_id>/messages/", MessagesApiView.as_view(), name="get_messages"),
    path("chat/message/<int:pk>/", UpdateDeleteMessageApiView.as_view(), name="update_delete_message"),
    path("chat/saved_chats/<int:pk>/", DeleteSavedChatApiView.as_view(), name="delete_saved_chats"),
]
