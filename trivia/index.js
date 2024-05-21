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

let inputField = document.querySelector('input');
let button = document.getElementById("btn_check");
let feedback = document.getElementById("feedback2");


// The correct answer
let correctAnswers = ["3", "three"];
inputField.addEventListener('input', function() {
    // Reset input field color and feedback message when a new answer is entered
    inputField.style.backgroundColor = '';
    feedback.textContent = '';
});

// Add click event listener to the button
button.addEventListener('click', function() {
    // Check if the answer is correct
    if (correctAnswers.includes(inputField.value.toLowerCase())) {
        // If the answer is correct, change the input field color to green
        inputField.style.backgroundColor = 'green';
        // Display "Correct!" message
        feedback.textContent = 'Correct!';
    } else {
        // If the answer is incorrect, change the input field color to red
        inputField.style.backgroundColor = 'red';
        // Display "Incorrect" message
        feedback.textContent = 'Incorrect';
    }
});
