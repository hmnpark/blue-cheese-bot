import urllib.parse
import json
import requests


BASE_URL = 'https://uci.campusdish.com/api/menu/GetMenus?'


def get_menu_from_campusdish_api(locationId: str, date: str, periodId: str) -> dict:
    """
    Returns api response as a dict, or None.

    :param str locationId: 3314 = Brandywine, 3056 = The Anteatery
    :param str date: mm/dd/yyyy
    :param str periodId: 49 = Breakfast, 106-108 = Lunch, Dinner, Late Night
    :return dict: dict of api response
    """
    url = BASE_URL + urllib.parse.urlencode(
        [('locationId', locationId), ('Mode', 'Daily'), ('date', date), ('periodId', periodId)])
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None


if __name__ == '__main__':
    # print(get_menu_from_campusdish_api('3314', '10/01/2021', '106'))
    pass
