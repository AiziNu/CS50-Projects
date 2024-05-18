import re

def get_string(prompt):
    return input(prompt)

def calculate_readability():
    text = get_string("Enter some text: ")
    letters = len(re.findall(r'[a-zA-Z]', text))

    words = len(re.findall(r'\b\w+\b', text))

    sentences = text.count('.')+ text.count('?') + text.count('!')

    L = (letters / words) *100
    S = (sentences / words) * 100

    grade = round(0.0588 * L - 0.296 * S - 15.8)

    if grade < 1:
      print("Before Grade 1")
    elif grade >=16:
     print("Grade 16+")
    else:
     print(f"Grade {grade} ")

calculate_readability()

