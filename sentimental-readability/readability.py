import re

def get_string(prompt):
    return input(prompt)

def calculate_readability():
    text = get_string("Enter some text: ")

    # Count the number of letters
    letters = len(re.findall(r'[a-zA-Z]', text))

    # Count the number of words
    words = len(re.findall(r'\b\w+\b', text))

    # Count the number of sentences
    sentences = text.count('.') + text.count('!') + text.count('?')

    # Calculate the average number of letters and sentences per 100 words
    L = (letters / words) * 100
    S = (sentences / words) * 100

    # Calculate the grade level using the Coleman-Liau formula
    index = 0.0588 * L - 0.296 * S - 15.8
    index = int(index) if index - int(index) < 0.5 else int(index) + 1

    # Print the grade level
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")

calculate_readability()

