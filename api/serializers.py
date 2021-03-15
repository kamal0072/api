from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=18)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)