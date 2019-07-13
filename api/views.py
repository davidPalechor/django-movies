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
        queryset = Movie.objects.all()

        for movie in queryset:
            data.append({
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