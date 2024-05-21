// Get all the buttons
var buttons = document.querySelectorAll('button');

// Add event listener to each button
buttons.forEach(function(button) {
    button.addEventListener('click', function() {
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
