""" The amount of minutes the it is baking in the oven."""
EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):
    """Return remaining baking time in minutes

    Parameter:
    The function that takes the actual minutes the lasagna has been in the oven

    Returns:
    How many minutes the lasagna still needs to bake based on the EXPECTED_BAKE_TIME.

    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Returns total preparation time in minutes

    Parameter:
    The function that takes the number of layers you want to add to the lasagna as an argument

    Returns:
    How many minutes you would spend making them

    """

    return 2* int(number_of_layers)

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Returns elapsed cooking time in minutes

    Parameter:
    The function has two parameters:number_of_layers and elapsed_bake_time

    Returns:
    The total number of minutes you've been cooking

    """

    return (2* int(number_of_layers)) + int(elapsed_bake_time)
