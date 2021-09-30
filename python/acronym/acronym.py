def abbreviate(words):
    abbreviation = ""
    disallowed_characters = ("-","_")
    for disallowed_character in disallowed_characters:
        words = words.replace(disallowed_character, " ")
    word_split = words.split(" ")
    stripped_sentence = [word.strip(" ") for word in word_split if word]
    for word in stripped_sentence:
        abbreviation += word[0].upper()
    return abbreviation

