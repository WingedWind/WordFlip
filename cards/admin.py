"""Admin configuration for flashcard models."""
from django.contrib import admin

from .models import Deck, Flashcard


@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    """Admin settings for deck objects."""

    list_display = ('id', 'title', 'created_at')
    search_fields = ('title',)
    ordering = ('title',)


@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    """Admin settings for flashcard objects."""

    list_display = ('id', 'term', 'deck', 'created_at')
    list_filter = ('deck', 'created_at')
    search_fields = ('term', 'meaning', 'deck__title')
    ordering = ('deck', 'term')
