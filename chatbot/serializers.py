from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=500)
    user_id = serializers.CharField(max_length=100)
