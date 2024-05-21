// Get all the buttons
let buttons = document.querySelectorAll('button');

buttons.forEach(button => {
    button.addEventListener('click', function() {
        // Reset color of all buttons to default
        buttons.forEach(function(otherButton) {
            otherButton.style.backgroundColor = ''; // Empty string sets it to default
        });

        // Check if the answer is correct
        if (button.classList.contains('correct')) {
            // If the answer is correct, change the button color to green
            button.style.backgroundColor = 'green';
            // Display "Correct!" message
            document.getElementById('feedback1').textContent = 'Correct!';
        } else {
            // If the answer is incorrect, change the button color to red
            button.style.backgroundColor = 'red';
            // Display "Incorrect" message
            document.getElementById('feedback1').textContent = 'Incorrect';
        }
    });
});



