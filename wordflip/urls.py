"""Root URL configuration for the WordFlip project."""
from django.urls import include, path

urlpatterns = [
    path('', include('cards.urls')),
]
