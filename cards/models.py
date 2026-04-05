"""Domain models for the WordFlip application."""
from django.db import models


class Deck(models.Model):
    """A thematic set of flashcards."""

    title = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Flashcard(models.Model):
    """A single learning item inside a deck."""

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    term = models.CharField(max_length=128)
    meaning = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.term} — {self.meaning}"
