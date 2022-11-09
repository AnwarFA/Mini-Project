"""MiniProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movielist import views
from movielist.views import RegisterView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        "movie/<int:movie_id>/",
        views.MovieDetails.as_view(),
        name="movie-details",
    ),
    path(
        "movie/<int:movie_id>/update/",
        views.UpdateMovie.as_view(),
        name="update-movie",
    ),
    path(
        "movie/<int:movie_id>/cancel/",
        views.CancelMovie.as_view(),
        name="cancel-movie",
    ),
    path("movielist/", views.MovieList.as_view(), name="movie-list"),
    path("signin/",views.SignInAPIView.as_view(), name="signin" ),
    path("book/<int:movie_id>/", views.BookMovie.as_view(), name="book-movie"),
    path("register/", RegisterView.as_view(), name="register"),
    path("token/refresh/", TokenRefreshView.as_view(), name='token-referesh'),
]
