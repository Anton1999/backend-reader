from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .models import Rate as RateModel
from .serializer import *


class BookView(APIView):
    def get(self, request):
        bk = Book.objects.all()

        serializer = BookSerializer(bk, many=True)
        return Response({"Книги": serializer.data})

class SearchView(APIView):
    def get(self, request,title):
        bk = Book.objects.filter(title__contains=title)
        
        serializer = BookSerializer(bk, many=True)

        return Response({"Результаты поиска" : serializer.data})

class OpenBookView(APIView):
    def get(self, request, title, id):
        OpenBook = Book.objects.filter(title=title)
        RateBook = RateModel.objects.filter(book=id)

        return Response(
    {
    'Книга': OpenBookSerializer(OpenBook, many=True).data, 
    'Отзывы': Rate(RateBook, many=True).data, 
  }
                        )


