from django.urls import path
from .views import play_game, intro
urlpatterns = [
    path('', intro, name='intro'),
    path('play/', play_game, name='play')
]