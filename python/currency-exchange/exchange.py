def estimate_value(budget, exchange_rate):

    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - estimated value of the foreign currency you can receive
    """
    return float(budget / exchange_rate)

def get_change(budget, exchanging_value):

    """

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging
    """

    return float(budget - exchanging_value)

def get_value(denomination, number_of_bills):

    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have
    """

    return float(denomination * number_of_bills)

def get_number_of_bills(budget, denomination):

    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money
    """

    return int(budget / denomination)


def exchangeable_value(budget, exchange_rate, spread, denomination):

    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get
    """

    real_exchange_rate = exchange_rate * (1 + spread/100)
    estimated_cash_value = estimate_value(budget , real_exchange_rate)
    number_of_bills = int(estimated_cash_value / denomination)
    return number_of_bills * denomination

def unexchangeable_value(budget, exchange_rate, spread, denomination):

    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - unexchangeable value
    """

    real_exchange_rate = exchange_rate * (1 + spread/100)
    estimated_cash_value = estimate_value(budget, real_exchange_rate)
    return int(estimated_cash_value % denomination)
