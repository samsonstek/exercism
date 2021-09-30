def is_pangram(sentence):
    result = set()
    for word in sentence:
        if word.isalpha():
            result.add(word.lower())
    return len(result) ==26
