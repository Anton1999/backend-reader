from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializer import *


class ProfileView(APIView):
    def get(self, request, username):
        us = User.objects.filter(username=username)

        serializer = ProfileSerializer(us, many=True)
        return Response(serializer.data)

class Favorite(APIView):
    def get(self, requets, username):

        fav = User.objects.filter(username=username).favorite.all()

        serializer = BookSerializer(fav, many= True)

        return Response(serializer.data)
