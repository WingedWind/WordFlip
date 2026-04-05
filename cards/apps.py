"""App configuration for the cards application."""
from django.apps import AppConfig


class CardsConfig(AppConfig):
    """Configuration for the flashcards app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cards'
    verbose_name = 'Cards'
