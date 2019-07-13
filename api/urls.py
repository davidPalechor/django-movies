from django.urls import path

from . import views


app_name = 'api'
urlpatterns = [
    path('movie/create_movie/', views.MovieCreateAPIView.as_view(), name='create_movie_api'),
    path('movie/list_movies/', views.MovieListAPIView.as_view(), name="list_movies_api"),
]