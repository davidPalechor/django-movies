from django.contrib.auth.models import User
from django.urls import reverse

from django_dynamic_fixture import G
from test_plus.test import TestCase

from .models import Movie


class MovieTestCase(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_user(
            username='demodemo',
            password='djangodev',
            is_superuser=True,
        )

        self.movie_thriller = G(
            Movie,
            title='Some slug',
            user=self.superuser,
            category='thriller',
            slug='some-slug',
        )

        self.movie_comedy = G(
            Movie,
            title='Comedy delete',
            user=self.superuser,
            category='comedy',
            slug='comedy-delete',
        )

    def test_get_movie_list(self):
        with self.login(username='demodemo', password='djangodev'):
            response = self.get('movie:list_movies')
            self.response_200()
            self.assertTrue('by demodemo' in response.content.decode())

    def test_create_movie(self):
        response = self.get('movie:create_movie')
        self.response_302
        self.assertRedirects(
            response,
            '{}?next=/movie/create_movie/'.format(reverse('user:login'))
        )

        with self.login(username='demodemo', password='djangodev'):
            payload = {
                "title": "The Shining",
                "director": "Stanley Kubrick",
                "writer": "same",
                "stars": "4",
                "summary": "Mad Mad at A Hotel",
                "year": "1976",
                "category": "thriller",
            }
            response = self.post('movie:create_movie', data=payload)

            self.response_302()
            self.assertRedirects(response, reverse('movie:list_movies'))
            self.assertTrue(Movie.objects.filter(slug='the-shining').exists())

    def test_update_movie(self):
        response = self.get(reverse('movie:edit_movie', kwargs={'slug':'some-slug'}))
        self.response_302()
        self.assertRedirects(
            response,
            '{}?next=/movie/some-slug/edit/'.format(reverse('user:login'))
        )

        with self.login(username='demodemo', password='djangodev'):
            payload = {
                "title": "The Godfather",
                "director": "Coppola",
                "writer": "writer",
                "stars": "4",
                "summary": "Mad Man at A Great Hotel",
                "year": "1976",
                "category": "thriller",
            }
            response = self.post(
                reverse('movie:edit_movie', kwargs={'slug':'some-slug'}),
                data=payload,
            )

            self.response_302()
            self.assertRedirects(response, reverse('movie:list_movies'))
            self.assertTrue(Movie.objects.filter(slug='the-godfather').exists())

    def test_delete_movie(self):
        response = self.get(
            reverse('movie:delete_movie', kwargs={'slug':'comedy-delete'})
        )
        self.response_302()
        self.assertRedirects(
            response,
            '{}?next=/movie/comedy-delete/delete/'.format(reverse('user:login'))
        )

        with self.login(username='demodemo', password='djangodev'):
            response = self.post(
                reverse('movie:delete_movie', kwargs={'slug':'comedy-delete'})
            )
            self.response_302()
            self.assertRedirects(response, reverse('movie:list_movies'))
            self.assertTrue(Movie.objects.get(slug='comedy-delete').deleted)
