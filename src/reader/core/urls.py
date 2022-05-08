from django.urls import path

from .views import *

app_name = "core"

urlpatterns = [
    path('profile/<str:username>', ProfileView.as_view()),
    path('favorite/<str:username>', Favorite.as_view())
]
