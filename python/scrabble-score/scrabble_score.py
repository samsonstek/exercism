SCRABBLE_SCORE = {
    1: 'AEIOULNRST', 
    2: 'DG', 
    3: 'BCMP', 
    4: 'FHVYW', 
    5: 'K', 
    8: 'JX', 
    10: 'QZ'
}
def score(word):
    word_score = 0
    for letter in word.upper():
        for key , value in SCRABBLE_SCORE.items():
            if letter in value:
                word_score += key
    return word_score
