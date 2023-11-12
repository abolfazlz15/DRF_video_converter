from rest_framework import serializers
from django.contrib.auth import authenticate, password_validation
from rest_framework_simplejwt.tokens import RefreshToken



class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    password = serializers.CharField(required=False)

    def validate(self, attrs):
        user = authenticate(**attrs)

        if user:
            return user
        raise serializers.ValidationError({'error': 'this user is not exist', 'success': False})

    def save(self, validated_data):
        refresh = RefreshToken.for_user(validated_data)
        return ({
            'username': validated_data.fullname,
            'user_id': validated_data.id,
            'refresh': str(refresh),
            'access': str(refresh.access_token),

        })