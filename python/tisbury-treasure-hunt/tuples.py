def get_coordinate(record):

    """

    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]

def convert_coordinate(coordinate):

    """

    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual components.
    """

    return (coordinate[0] , coordinate[1])
    #optionally
    #return tuple(coordinate)

def compare_records(azara_record, rui_record):

    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    """
    record_azara = tuple(azara_record[1])
    record_rui = rui_record[1]
    if record_azara == record_rui:
        return True
    return False

    #optionally
    # return convert_coordinate(get_coordinate(azara_record)) == rui_record[1]

def create_record(azara_record, rui_record):

    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    """

    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"

def clean_up(combined_record_group):

    """

    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: string of tuples separated by newlines - everything "cleaned". Excess coordinates and information removed.
    """

    result = ""
    for treasure_with_data_info in combined_record_group:
        treasure_with_data_location=(treasure_with_data_info[0],
        treasure_with_data_info[2],
        treasure_with_data_info[3],
        treasure_with_data_info[4]
        )
        result = result + str(treasure_with_data_location)+"\n"
        # Optionally result = result + f"{treasure_with_data_location}"+"\n"
    return result
