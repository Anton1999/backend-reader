from django.urls import path

from .views import *

app_name = "book"

urlpatterns = [
    path('all/', BookView.as_view()),
    path('search/<str:title>', SearchView.as_view()),
    path('<str:title>/<int:id>', OpenBookView.as_view())
]