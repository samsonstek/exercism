sounds = {3: "Pling" , 5: "Plang" , 7: "Plong"}

def convert(number):
    result = ""
    for divisor, sound in sounds.items():
        if number % divisor == 0:
            result += sound
    return result or str(number)