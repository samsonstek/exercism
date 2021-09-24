from typing import Counter


def create_inventory(items):
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """

    full_inventory = {}
    for list_of_item in items:
        if list_of_item in full_inventory:
            full_inventory[list_of_item] += 1
        else:
            full_inventory[list_of_item] = 1
    return full_inventory

def add_items(inventory, items):
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """

    for item_list in items:
        if item_list in inventory:
            inventory[item_list] += 1
        else:
            inventory[item_list] = 1
    return inventory

def decrement_items(inventory, items):

    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """

    for list_of_item in items:
        if list_of_item in inventory:
            if inventory[list_of_item] > 0:
                inventory[list_of_item] -= 1
    return inventory

def remove_item(inventory, item):

    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """

    if item in inventory:
        del inventory[item]
    return inventory

def list_inventory(inventory):

    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    result = []
    for key,value in inventory.items():
        if value > 0:
            result.append((key,value))
    return result
