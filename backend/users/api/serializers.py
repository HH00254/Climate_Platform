"""
Summary:
- Serializers for User model.
"""

from django.contrib.auth import authenticate

from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Summary:
    - Serializer for User model.
    """

    class Meta:
        """
        Summary:
        - Configuration for User serializer.
        """

        model = User

        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name"
        ]


class UserRegistrationSerializer(
    serializers.ModelSerializer
):
    """
    Summary:
    - Serializer for user registration.
    """

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={
            "input_type": "password"
        }
    )

    password_confirm = serializers.CharField(
        write_only=True,
        required=True,
        style={
            "input_type": "password"
        }
    )

    class Meta:
        """
        Summary:
        - Configuration for user registration serializer.
        """

        model = User

        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "password_confirm"
        ]

    def validate_email(self, email):
        """
        Summary:
        - Validate that email is unique.
        """

        if User.objects.filter(
            email=email
        ).exists():

            raise serializers.ValidationError(
                "A user with this email already exists."
            )

        return email

    def validate_username(self, username):
        """
        Summary:
        - Validate that username is unique.
        """

        if User.objects.filter(
            username=username
        ).exists():

            raise serializers.ValidationError(
                "A user with this username already exists."
            )

        return username

    def validate(self, attrs):
        """
        Summary:
        - Validate registration data.
        """

        if (
            attrs["password"]
            != attrs["password_confirm"]
        ):
            raise serializers.ValidationError(
                {
                    "password_confirm":
                    "Passwords do not match."
                }
            )

        return attrs

    def create(self, validated_data):
        """
        Summary:
        - Create a new user.
        """

        validated_data.pop(
            "password_confirm"
        )

        return User.objects.create_user(
            **validated_data
        )


class UserLoginSerializer(
    serializers.Serializer
):
    """
    Summary:
    - Serializer for user login.
    """

    username = serializers.CharField(
        required=True
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={
            "input_type": "password"
        }
    )

    def validate(self, attrs):
        """
        Summary:
        - Validate user credentials.
        """

        username = attrs.get(
            "username"
        )

        password = attrs.get(
            "password"
        )

        user = authenticate(
            username=username,
            password=password
        )

        if user is None:
            raise serializers.ValidationError(
                "Invalid username or password."
            )

        attrs["user"] = user

        return attrs