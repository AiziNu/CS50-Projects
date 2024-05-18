import re


def calculate_readability(text):
    letters = len(re.findall(r'\b\w\b', text))

    words = len(re.findall(r'\b\w+\b', text))

    sentences = text.count('.')+ text.count('?') + text.count('!')

    L = (letters / words) *100
    S = (sentences / words) * 100

    grade = round()
