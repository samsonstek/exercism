def steps(number):
    if number < 0 or number == 0:
        raise ValueError("The number should not be equal to zero or Negative")
    counter = 0
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        counter += 1
    return counter
