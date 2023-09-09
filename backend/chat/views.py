from chat.models import Chat, Message
from chat.permissions import (IsCreatorOrReadOnly,
                              IsSenderOrReadOnly,
                              IsOnlyDescriptionInRequestData,
                              IsEmailConfirm,
                              IsOnlyTextInRequestData)
from chat.serializer import ChatSerializer, MessageSerializer
from config.settings import CHOICE_ROOM
from rest_framework import generics, status
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ChatAPIView(generics.GenericAPIView):
    """API to get/put chat"""

    permission_classes = (IsAuthenticated, IsEmailConfirm)
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    serializer_class = ChatSerializer
    http_method_names = ["get", "post"]

    def get(self, request, room_name):
        """Get chat list from the certain room"""

        # if wrong room name
        if (room_name, room_name) not in CHOICE_ROOM:
            return Response({"Error": "wrong room"}, status=status.HTTP_400_BAD_REQUEST)

        # get chats, serialize, and return list of chats by pagination
        self.queryset = Chat.objects.filter(room=room_name)
        serializer = ChatSerializer(self.queryset, context={"request": request}, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)

    def post(self, request, room_name):
        """Create Chat"""

        data = request.data.copy()
        data["room"] = room_name
        serializer = ChatSerializer(data=data)

        if serializer.is_valid():
            # Optional fields
            img = request.data.get("img", None)
            description = request.data.get("description", None)

            new_chat = Chat.objects.create(
                title=request.data["title"],
                room=room_name,
                creator=request.user,
                img=img,
                description=description,
            )
            serializer.update_url(obj=new_chat)
            return Response(
                {"chat": ChatSerializer(new_chat, context={"request": request}).data}, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteChatApiView(generics.RetrieveUpdateDestroyAPIView):
    """Update chat description or delete chat"""

    permission_classes = (IsAuthenticated, IsCreatorOrReadOnly, IsOnlyDescriptionInRequestData, IsEmailConfirm)
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    http_method_names = ["patch", "delete"]


class MessagesApiView(generics.ListAPIView):
    """Get messages from the certain chat"""

    permission_classes = (IsAuthenticated, IsEmailConfirm)
    serializer_class = MessageSerializer
    http_method_names = ["get"]

    def get_queryset(self):
        """Get messages from the certain chat"""

        chat_id = self.kwargs["chat_id"]
        return Chat.objects.get(pk=chat_id).message_set.all()


class UpdateMessageApiView(generics.RetrieveUpdateDestroyAPIView):
    """Update text of message"""

    permission_classes = (IsAuthenticated, IsOnlyTextInRequestData, IsSenderOrReadOnly, IsEmailConfirm)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    http_method_names = ["patch"]
