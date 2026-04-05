"""Forms for creating and editing flashcards."""
import re

from django import forms

from .models import Deck, Flashcard


class FlashcardForm(forms.ModelForm):
    """Form for creating and editing flashcards."""

    new_deck = forms.CharField(
        max_length=128,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Например: Web Development',
                'class': 'input-field',
            }
        ),
    )

    class Meta:
        model = Flashcard
        fields = ['term', 'meaning', 'deck']
        widgets = {
            'term': forms.TextInput(
                attrs={
                    'placeholder': 'Например: Polymorphism',
                    'class': 'input-field input-large',
                }
            ),
            'meaning': forms.Textarea(
                attrs={
                    'placeholder': 'Кратко объясни значение термина',
                    'class': 'input-field input-area',
                }
            ),
            'deck': forms.Select(
                attrs={'class': 'input-field'}
            ),
        }

    def __init__(self, *args, **kwargs):
        """Initialize the form and configure the deck field."""
        super().__init__(*args, **kwargs)
        self.fields['deck'].queryset = Deck.objects.all()
        self.fields['deck'].required = False
        self.fields['deck'].empty_label = 'Выбери набор'

    def clean_term(self):
        """Validate the flashcard term field."""
        term = self.cleaned_data.get('term', '').strip()

        if not term:
            raise forms.ValidationError(
                'Термин должен содержать от 1 до 32 символов.'
            )

        if not re.fullmatch(r'[a-zA-Zа-яА-ЯёЁ\s\-]+', term):
            raise forms.ValidationError(
                'Термин может содержать только русские или английские буквы.'
            )

        return term

    def clean_meaning(self):
        """Validate the flashcard meaning field."""
        meaning = self.cleaned_data.get('meaning', '').strip()

        if not meaning:
            raise forms.ValidationError(
                'Пояснение должно содержать от 1 до 128 символов.'
            )

        return meaning

    def clean_new_deck(self):
        """Validate the optional new deck name."""
        new_deck = self.cleaned_data.get('new_deck', '').strip()

        if new_deck and not re.fullmatch(
            r'^[a-zA-Zа-яА-ЯёЁ\s\-]+$',
            new_deck
        ):
            raise forms.ValidationError(
                'Название набора может содержать только буквы, пробелы и дефисы.'
            )

        return new_deck

    def clean(self):
        """Validate that a deck is selected or a new one is provided."""
        cleaned_data = super().clean()

        deck = cleaned_data.get('deck')
        new_deck = cleaned_data.get('new_deck', '').strip()

        if not deck and not new_deck:
            raise forms.ValidationError(
                'Выберите существующий набор или введите новый.'
            )

        return cleaned_data
