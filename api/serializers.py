from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Portfolio


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class PortfolioSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.name', read_only=True)

    class Meta:
        model = Portfolio
        fields = ('id', 'title', 'description', 'image', 'github', 'user')
