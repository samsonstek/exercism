from unittest import result
from unittest.signals import registerResult
def get_rounds(number):

    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """

    result = []
    for value in range(number, number+3):
        result.append(value)
    return result
    
def concatenate_rounds(rounds_1, rounds_2):

    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    for value in rounds_2:
        rounds_1.append(value)
    return rounds_1

def list_contains_round(rounds, number):

    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    if number in rounds:
        return True
    return False

def card_average(hand):

    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    return float(sum(hand)/len(hand))

def approx_average_is_average(hand):

    """

    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    """

    average = card_average(hand)
    if (hand[0]+ hand[-1])/2 == average:
        return True
    return False

def average_even_is_average_odd(hand):

    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even_position = hand[0::2]
    odd_position = hand[1::2]
    if card_average(even_position) == card_average(odd_position):
        return True
    return False

def maybe_double_last(hand):
    
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = hand[-1] *2 
    return hand