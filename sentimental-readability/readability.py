import re


def calculate_readability(text):
    letters = len(re.findall(r'\b\w\b', text))

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
     print("Grade", grade)

def main():
    text = input("Enter some text: ")
    calculate_readability(text)

main()
