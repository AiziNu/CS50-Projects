// Get the button
let button = document.getElementById('main_btn');

// Add event listener to the button
button.addEventListener('click', function() {
    // Redirect to another website
    window.location.href = 'https://www.example.com';

    // Or change the background image of the webpage
    document.body.style.backgroundImage = "url('path-to-your-image.jpg')";
});
