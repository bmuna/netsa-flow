
from rest_framework import serializers
from users.models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name"]
        extra_kwargs = {"password": {"write_only": True}} # Ensures the password is not returned in the response


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    # As DRF saves the password in plain text, we need to override the create method to hash the password before saving in the database