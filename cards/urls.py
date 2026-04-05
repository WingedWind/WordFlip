"""URL routes for the flashcards application."""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flashcards/', views.flashcards_list, name='flashcards-list'),
    path('flashcards/new/', views.add_flashcard, name='add-flashcard'),
    path(
        'flashcards/<int:flashcard_id>/edit/',
        views.edit_flashcard,
        name='edit-flashcard',
    ),
    path('practice/', views.practice_decks, name='practice'),
    path(
        'practice/<int:deck_id>/',
        views.practice_session,
        name='practice-session',
    ),
]
