from chat.models import Chat, Message
from rest_framework import serializers


class ChatSerializer(serializers.ModelSerializer):
    """Chat Serializer"""

    creator = serializers.SerializerMethodField(source="get_creator")
    img = serializers.SerializerMethodField(source="get_img")

    class Meta:
        model = Chat
        fields = ["id", "title", "room", "img", "creator", "description", "url", "timestamp"]
        extra_kwargs = {"id": {"read_only": True}, "creator": {"read_only": True}}

    def update_url(self, obj, *args, **kwargs):
        """Update chat to save url with id"""

        obj.url = f"/chat/{obj.room}/{obj.pk}/"
        obj.save()
        return obj

    def get_creator(self, obj):
        """Return creator username (instead id)"""

        if obj.creator:
            return obj.creator.username
        else:
            # if user was deleted
            return "Unknown"

    def get_img(self, obj):
        """Return absolute url of chat img"""

        request = self.context.get("request")
        return request.build_absolute_uri(obj.img.url)


class MessageSerializer(serializers.ModelSerializer):
    """Serializer for websocket messages"""

    class Meta:
        model = Message
        fields = ["id", "chat", "user", "text", "timestamp"]
        extra_kwargs = {"timestamp": {"read_only": True}, "user": {"read_only": True}}

    def create(self, validated_data):
        """Save message with user"""

        user = self.context.get("user")
        validated_data["user"] = user
        return super().create(validated_data)


class WebsocketMessageSerializer(serializers.Serializer):
    """Serializer for websocket messages"""

    message = MessageSerializer()
    type = serializers.CharField()

    class Meta:
        fields = ["type", "message"]
