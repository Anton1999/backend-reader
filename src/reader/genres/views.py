from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import *
from rest_framework import generics

from book.models import *
from .serializer import BookSerializer, GenreSerializer, OpenBookSerializer

class GenreView(generics.ListAPIView):
    def get(self, request, name):

        if name == 'all':
            gnr = Genre.objects.filter()
            serializer = GenreSerializer(gnr, many=True)

            return Response({'Жанры': serializer.data}) # Пока срез на 2(я помню, что ты говорил 10), так надо, чтобы ты видел, что все работает

        g = Genre.objects.filter(name=name)
        gnr = g.get(name=name).id


        gnr = Book.objects.filter(genre=gnr)
        serializer = BookSerializer(gnr, many=True)


        return Response({'Жанры': serializer.data})

class All(APIView):
    def get(self, request):

        gnr = Genre.objects.all()
        serializer = GenreSerializer(gnr, many=True)
        return Response({'Жанры':serializer.data})


class Open(APIView):
    def get(self, request, id, name, title):
        g = Genre.objects.filter(name=name)
        gnr = g.get(name=name).id

        book = Book.objects.filter(genre=gnr)

        return Response(OpenBookSerializer(book, many=True).data)
