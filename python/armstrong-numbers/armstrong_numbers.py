def is_armstrong_number(number):
    counter = 0
    for numbers in str(number):
        counter += int(numbers) ** len(str(number))
    if counter == number:
        return True
    return False

