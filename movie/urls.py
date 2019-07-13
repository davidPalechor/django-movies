from django.urls import path

from . import views


app_name = 'movie'
urlpatterns = [
    path('create_movie/', views.MovieCreateView.as_view(), name='create_movie'),
    path('list_movies/', views.MovieListView.as_view(), name='list_movies'),
    path('<slug>/edit/', views.MovieEditView.as_view(), name='edit_movie'),
    path('<slug>/delete/', views.MovieDeleteView.as_view(), name='delete_movie')
]
