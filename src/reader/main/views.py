from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import *
from .serializer import BookSerializer, GenreSerializer


class GenreAllView(APIView):
    def get(self, request):

        gnr = Genre.objects.all()
        serializer = GenreSerializer(gnr, many=True)

        genre = {'Комедия': 1, 'Драма': 2, 'Детектив': 3, 'Роман': 4}
        
        return Response({"Жанры": serializer.data[:10]})

