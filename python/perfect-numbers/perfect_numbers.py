def classify(number):
    if number < 0 or number == 0:
        raise ValueError("The number should not be equal to zero or Negative")
    counter = 0
    for numbers in range(1, number):
        if number % numbers == 0:
            counter += numbers
    if counter == number:
        return "perfect"
    if counter > number:
        return "abundant"
    if counter < number:
        return "deficient"
