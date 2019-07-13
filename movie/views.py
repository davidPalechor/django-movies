from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.db import IntegrityError

from .forms import MovieCreationForm
from .models import Movie



class MovieListView(ListView):
    model = Movie
    queryset = Movie.objects.filter(deleted=False).order_by("-stars")
    template_name = "movie_list.html"
    paginate_by = 10


class MovieCreateView(LoginRequiredMixin, CreateView):
    form_class = MovieCreationForm
    login_url = reverse_lazy('user:login')
    model = Movie
    redirect_field_name = 'next'
    success_url = reverse_lazy('movie:list_movies')
    template_name = 'create_movie.html'

    def form_valid(self, form):
        try:
            movie = form.save(commit=False)
            movie.user = self.request.user
            movie.save()

            return super().form_valid(form)
        except IntegrityError:
            form.add_error(
                None,
                'Movie already exists.'
            )
            return self.form_invalid(form)


class MovieEditView(LoginRequiredMixin, UpdateView):
    form_class = MovieCreationForm
    login_url = reverse_lazy('user:login')
    model = Movie
    redirect_field_name = 'next'
    success_url = reverse_lazy('movie:list_movies')
    template_name = 'create_movie.html'


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('movie:list_movies')
    model = Movie
    login_url = reverse_lazy('user:login')
    redirect_field_name = 'next'
    template_name = 'movie_confirm_delete.html'
    context_object_name = 'movie'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()
        return HttpResponseRedirect(self.get_success_url())