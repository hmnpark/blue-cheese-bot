LOCATIONS = {'3314': 'Brandywine', 'Brandywine': '3314', '32802': 'Ember/Grill', '32801': 'Grubb/ Mainline',
             '32806': 'Hearth/Pizza', '32807': 'Saute', '32808': 'Soups', '32809': 'The Farm Stand/ Deli',
             '32805': 'The Farm Stand/ Salad Bar', '32810': 'Vegan', '32803': 'Crossroads', '32811': 'Compass',
             '32804': 'Honeycakes/Bakery', '41195': 'La Latina Cocina', '42378': 'Promotions',
             '3056': 'The Anteatery', 'The Anteatery': '3056', '23992': 'Deli', '23994': 'Bakery', '23989': 'Home',
             '23990': 'Sizzle Grill', '23991': 'Oven', '23993': "Farmer's Market", '23995': 'Fire And Ice Sauté',
             '30079': 'Soups', '23996': 'Vegan'}

PERIODS = {'49': 'Breakfast', 'Breakfast': '49',
           '106': 'Lunch', 'Lunch': '106',
           '107': 'Dinner', 'Dinner': '107',
           '108': 'Late Night', 'Late Night': '108'}


def stationids_to_names(stations: list) -> dict:
    """
    Maps station Id's to their names.
    Can be used to get an up-to-date mapping of station mappings.

    :param list stations: API_RES['Menu']['MenuStations]
    :return dict station_name_mapping: station ids as keys, their names as values
    """
    station_name_mapping = dict()
    for station in stations:
        station_name_mapping[station['StationId']] = station['Name']

    return station_name_mapping
