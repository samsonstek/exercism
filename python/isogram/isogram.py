def is_isogram(string): 
    lowercase_string = string.lower()
    for alphabet in lowercase_string:
        if lowercase_string.count(alphabet) > 1 and alphabet.isalpha():
            return False
    return True
