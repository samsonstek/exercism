from typing import Counter
import re


def count_words(sentence):
    disallowed_characters=(",","\n",".",":","!","&","$","%","^","@","_","\t")
    for disallowed_character in disallowed_characters:
        sentence = sentence.replace(disallowed_character, " ")
    split_sentence = sentence.split(" ")
    stripped_sentence=[word.strip("'") for word in split_sentence if word]

    lowercase_character =[character.lower() for character in stripped_sentence]
    return dict(Counter(lowercase_character))
