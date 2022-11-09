from django.shortcuts import render
from movielist.models import Movie
# Create your views here.
import datetime
from rest_framework.response import Response
from rest_framework import generics
from .serializers import SignInSerializer, RegisterSerializer
from movielist import serializers
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser 


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class SignInAPIView(APIView):
    serializer_class = SignInSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        data = request.data
        serializer = SignInSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, HTTP_400_BAD_REQUEST)

class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieListSerializer
    permission_classes = [IsAuthenticated]


class MovieDetails(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieDetailsSerializer
    lookup_url_kwarg = "movie_id"


class UpdateMovie(generics.RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = serializers.UpdateMovieSerializer
    lookup_url_kwarg = "movie_id"
    parser_classes = [IsAuthenticated]


class CancelMovie(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    lookup_url_kwarg = "movie_id"

class BookMovie(generics.CreateAPIView):
    serializer_class = serializers.UpdateMovieSerializer
    lookup_field = "id"
    lookup_url_kwarg = "movie_id"
    def perform_create(self, serializer):
        movie_id =self.kwargs["movie_id"]
        serializer.save(user=self.request.user, movie_id=movie_id)

