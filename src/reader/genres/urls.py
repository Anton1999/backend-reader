from django.urls import path
from .views import *

app_name = "genre"

urlpatterns = [
    path('genre/all', All.as_view()),
    path('genre/<str:name>', GenreView.as_view()),
    path('genre/<str:name>/<str:title>/<int:id>', Open.as_view())
]
