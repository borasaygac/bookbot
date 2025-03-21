import string
from typing import Dict, List

def count_words(text_from_book) -> int:
    num_words = len(text_from_book.split())
    return num_words

def count_character(text_from_book: str) -> dict[str, int]:

    text_from_book = text_from_book.lower()

    d = {}

    for char in text_from_book:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1

    return d
        
def sort_key_get(dictionary):
    return dictionary["frequency"]

def freq_sorter(frequencies) -> list:

    frequencies_list = [{"char": char, "frequency": frequencies[char]} for char in frequencies]
    frequencies_list.sort(reverse=True, key=sort_key_get)

    return frequencies_list



