from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["userID", "password","username","email"]

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        userID = validated_data["userID"]
        email = validated_data["email"]
        new_user = User(username=username, password=password, userID=userID, email=email)
        new_user.set_password(password)
        new_user.save()
        return validated_data

User = get_user_model()

class SignInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only = True, allow_blank = True)
    
    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
    

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("This username does not exist !!!")

        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect username and password !!")

        payload = RefreshToken.for_user(user)
        token = str(payload.access_token)

        data["access"] = token

        return data
    def get_token(cls, user):
        token = super().get_token(user)
        token["userID"] = user.userID
        token["username"] = user.username
        token["email"] = user.email
        token["password"] = user.password

        return token


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["movie", "time", "price", "id"]

class MovieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["movie", "date", "watchers", "id"]


class UpdateMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["date", "watchers"]
