from rest_framework import serializers


class ApplicationSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    access_token = serializers.UUIDField()
