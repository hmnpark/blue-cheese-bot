from collections import defaultdict
from .mappings import LOCATIONS


def parse_menu(unprocessed_menu: dict) -> dict:
    """
    Parses the API call to Brandywine or Anteatery into a dict.
    Key = station name, value = list of foods.

    :param dict unprocessed_menu: dict of api call
    :return dict: mapping of stations to the foods they have
    """
    unprocessed_foods = unprocessed_menu['Menu']['MenuProducts']
    menu = defaultdict(list)
    for food in unprocessed_foods:
        food_name = food['Product']['MarketingName']#.lower()
        try:
            station = LOCATIONS[food["StationId"]]
        except KeyError:
            station = food["StationId"]
        menu[station].append(food_name)

    return menu
