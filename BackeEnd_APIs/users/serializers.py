from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'phone_number', 'bio', 'date_of_birth', 'date_joined', 'raw_password')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'date_joined': {'read_only': True},
            'raw_password': {'read_only': True}
        }

    def create(self, validated_data):
        password = validated_data.get('password')
        user = User.objects.create_user(**validated_data)
        user.raw_password = password  # Store the raw password
        user.save()
        return user