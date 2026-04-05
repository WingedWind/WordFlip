"""Views for the WordFlip application."""
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FlashcardForm
from .models import Deck, Flashcard


def home(request):
    """Render the landing page."""
    return render(request, 'index.html')


def flashcards_list(request):
    """Display flashcards with optional deck filter."""
    deck_id = request.GET.get('deck_id')
    decks = Deck.objects.all()

    if deck_id and deck_id != 'all':
        selected_deck = get_object_or_404(Deck, id=deck_id)
        flashcards = Flashcard.objects.filter(deck=selected_deck)
    else:
        selected_deck = None
        flashcards = Flashcard.objects.select_related('deck').all()

    return render(
        request,
        'flashcards/list.html',
        {
            'decks': decks,
            'flashcards': flashcards,
            'selected_deck': selected_deck,
        },
    )


def add_flashcard(request):
    """Create a new flashcard."""
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            flashcard = form.save(commit=False)
            new_deck = form.cleaned_data['new_deck']

            if new_deck:
                deck, _ = Deck.objects.get_or_create(title=new_deck)
                flashcard.deck = deck

            flashcard.save()
            return redirect('add-flashcard')
    else:
        form = FlashcardForm()

    return render(
        request,
        'flashcards/add.html',
        {
            'form': form,
            'decks': Deck.objects.all(),
        },
    )


def edit_flashcard(request, flashcard_id):
    """Edit an existing flashcard."""
    flashcard = get_object_or_404(Flashcard, id=flashcard_id)

    if request.method == 'POST':
        form = FlashcardForm(request.POST, instance=flashcard)
        if form.is_valid():
            updated_flashcard = form.save(commit=False)
            new_deck = form.cleaned_data['new_deck']

            if new_deck:
                deck, _ = Deck.objects.get_or_create(title=new_deck)
                updated_flashcard.deck = deck

            updated_flashcard.save()
            return redirect('flashcards-list')
    else:
        form = FlashcardForm(instance=flashcard)

    return render(
        request,
        'flashcards/edit.html',
        {
            'form': form,
            'flashcard': flashcard,
            'decks': Deck.objects.all(),
        },
    )


def practice_decks(request):
    """Show decks available for practice mode."""
    decks = Deck.objects.all()
    return render(
        request,
        'practice/exam_collections.html',
        {
            'decks': decks,
        },
    )


def practice_session(request, deck_id):
    """Run practice mode for a selected deck."""
    selected_deck = get_object_or_404(Deck, id=deck_id)
    flashcards = list(Flashcard.objects.filter(deck=selected_deck))

    return render(
        request,
        'practice/exam_session.html',
        {
            'deck': selected_deck,
            'flashcards': flashcards,
        },
    )
