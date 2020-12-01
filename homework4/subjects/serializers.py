from rest_framework import serializers
from .models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    professors = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = ['id', 'name', 'credits', 'professors', 'created_at', 'updated_at']
