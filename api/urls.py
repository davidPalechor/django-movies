from django.urls import path

from . import views


app_name = 'api'
urlpatterns = [
    path('movie/create_movie/', views.MovieCreateAPIView.as_view(), name='create_movie_api'),
    path('movie/list_movies/', views.MovieListAPIView.as_view(), name="list_movies_api"),
    path('movie/<int:id>/edit_movie/', views.MovieUpdateAPIView.as_view(), name='update_movie_api'),
    path('movie/<int:id>/delete_movie/', views.MovieDeleteAPIView.as_view(), name='delete_movie_api'),
]
