import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from rest_framework.views import APIView

from movie.models import Movie


class MovieCreateAPIView(APIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        json_body = json.loads(request.body)

        user = User.objects.get(username=json_body['username'])

        Movie.objects.create(
            title=json_body['title'],
            director=json_body['director'],
            writer=json_body['writer'],
            stars=json_body['stars'],
            summary=json_body['summary'],
            year=json_body['year'],
            category=json_body['category'],
            user=user,
        )

        return HttpResponse('success', status=200)


class MovieListAPIView(APIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        data = []
        queryset = Movie.objects.filter(deleted=False)

        for movie in queryset:
            data.append({
                'id': movie.id,
                'title': movie.title,
                'director': movie.director,
                'writer': movie.writer,
                'stars': movie.stars,
                'summary': movie.summary,
                'year': movie.year,
                'category': movie.category,
                'registered_by': movie.user.username,
                'created_at': movie.created_at,
            })

        return JsonResponse({'data': data})


class MovieUpdateAPIView(APIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        movie_id = kwargs.get('id', '')

        json_body = json.loads(request.body)

        if Movie.objects.filter(id=movie_id).exists() or movie_id != '':
            movie = Movie.objects.get(id=movie_id)
            movie.title = json_body['title']
            movie.director = json_body['director']
            movie.writer = json_body['writer']
            movie.stars = json_body['stars']
            movie.summary = json_body['summary']
            movie.year = json_body['year']
            movie.category = json_body['category']
            movie.save()

            return HttpResponse('success', status=200)
        return HttpResponse('Object not found', status=404)


class MovieDeleteAPIView(APIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        movie_id = kwargs.get('id', '')

        if Movie.objects.filter(id=movie_id).exists() or movie_id != '':
            movie = Movie.objects.get(id=movie_id)
            movie.deleted = True
            movie.save()

            return HttpResponse('success', status=200)
        return HttpResponse('Object not found', status=404)
