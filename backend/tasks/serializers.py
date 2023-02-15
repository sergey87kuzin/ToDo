from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import Task, User


class TaskSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Task

    def get_success_headers(self, data):
        try:
            return {'Access-Control-Allow-Origin': '*'}
        except (TypeError, KeyError):
            return {}


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('username', 'email', 'password')
        model = User

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
