const buttons = document.querySelectorAll(.answer).forEach(button=>{
    button.addEventListener('click', function(){
        let isCorrect = this.dataset.correct === 'true';
        this.className = isCorrect ? 'correct' : 'incorrect';
        document.getElementById('feedback1').textContent = isCorrect ? 'Correct!' : 'Incorrect';
    })
})
