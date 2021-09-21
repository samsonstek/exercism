def is_criticality_balanced(temperature, neutrons_emitted):

    """Verify criticality is balanced.

    :param temperature: int
    :param neutrons_emitted: int
    :return:  boolean True if conditions met, False if not

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """

    product_of_temp_and_neutron = temperature * neutrons_emitted
    if temperature < 800  and neutrons_emitted > 500 and product_of_temp_and_neutron < 500000:
        return True
    return False

def reactor_efficiency(voltage, current, theoretical_max_power):

    """Assess reactor efficiency zone.

    :param voltage: int
    :param current: int
    :param theoretical_max_power: int
    :return: str one of 'green', 'orange', 'red', or 'black'

    Efficiency can be grouped into 4 bands:

    1. green  ->   80-100% efficiency
    2. orange ->   60-79% efficiency
    3. red    ->   30-59% efficiency
    4. black  ->   <30% efficient

    These percentage ranges are calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """

    generated_power = int(voltage) * int(current)
    efficiency = float(generated_power/theoretical_max_power) * 100
    if efficiency >= 80:
        return "green"
    elif efficiency >= 60 and efficiency < 80:
        return "orange"
    elif efficiency >= 30 and efficiency < 60:
        return "red"
    return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):

    """Assess and return safety range.

    :param temperature:
    :param neutrons_produced_per_second:
    :param threshold:
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'

    - `temperature * neutrons per second` < 40% of threshold == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutron per second` is not in the above-stated ranges ==  'DANGER'
    """

    product_of_temp_and_neutrons_per_sec = temperature *neutrons_produced_per_second
    if product_of_temp_and_neutrons_per_sec < (0.4 * threshold):
        return "LOW"
    if (0.9 * threshold) <= product_of_temp_and_neutrons_per_sec <= (1.1 * threshold):
        return "NORMAL"
    return "DANGER"
