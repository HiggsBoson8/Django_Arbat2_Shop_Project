from .utils import generate_activation_code, send_verification_mail
from .models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style = {'input_type': 'password'})

    class Meta:
        model = User
        fields = ('id', 'email', 'username',
        'password', 'phone', 'is_active', 'is_staff')

        extra_kwargs = {'password': {'write_only': True},
                        'email': {'write_only': True},
                        'phone': {'write_only': True},
                        'is_active': {'write_only': True},
                        'is_staff': {'write_only': True}} 

    def create(self, validated_data):
        code = generate_activation_code()
        user = User(
            email = validated_data['email'],
            username = validated_data['username'],
            phone = validated_data['data'],
            code = code)
        user.set_password(validated_data['password'])
        user.save()
        send_verification_mail(user.email, user.code) 
        return user 

class CodeSerializer(serializers.Serializer):
    code = serializers.IntegerField()
    email = serializers.EmailField()

class ResendCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style = {'input': 'password'},
        write_only = True)

        