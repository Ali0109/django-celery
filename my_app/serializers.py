from rest_framework import serializers
from . import models, tasks


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Data
        fields = "__all__"

    def create(self, validated_data):
        tasks.create_data.delay(validated_data['title'])
        return validated_data
