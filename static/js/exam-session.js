document.addEventListener('DOMContentLoaded', function () {
    const wordEl = document.getElementById('exam-word');
    const answerEl = document.getElementById('exam-answer');
    const cardEl = document.getElementById('exam-card');
    const progressEl = document.getElementById('exam-progress');

    let current = 0;
    let showAnswer = false;

    function renderCard() {
        if (current >= cards.length) {
            wordEl.classList.add('hidden');
            answerEl.classList.remove('hidden');
            answerEl.innerText = "Экзамен завершен!";
            progressEl.innerText = "";
            cardEl.style.cursor = "default";
            return;
        }

        wordEl.innerText = cards[current].word;
        answerEl.innerText = cards[current].explanation;

        wordEl.classList.remove('hidden');
        answerEl.classList.add('hidden');
        showAnswer = false;
        progressEl.innerText = `Карточка ${current + 1} из ${cards.length}`;
    }

    cardEl.addEventListener('click', () => {
        if (current >= cards.length) return;

        if (!showAnswer) {
            wordEl.classList.add('hidden');
            answerEl.classList.remove('hidden');
            cardEl.classList.add('card-explanation-show')
            showAnswer = true;
        } else {
            cardEl.classList.remove('card-explanation-show')
            current++;
            renderCard();
        }
    });

    renderCard();
});

