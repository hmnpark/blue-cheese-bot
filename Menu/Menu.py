from .parse import parse_menu
from .campusdish_api import get_menu_from_campusdish_api
from .mappings import LOCATIONS, PERIODS
import datetime
from datetime import datetime as dt


TIMEZONE = datetime.timezone(-datetime.timedelta(hours=8))


class Menu:
    def __init__(self):
        self.today = _get_today_as_str()
        self.brandywine = {'name': 'Brandywine', 'Breakfast': dict(), 'Lunch': dict(), 'Dinner': dict()}
        self.anteatery = {'name': 'The Anteatery', 'Breakfast': dict(), 'Lunch': dict(), 'Dinner': dict()}
        self._fetch_menus()

    def update_menu(self):
        if self.today != _get_today_as_str():
            self.today = _get_today_as_str()
            self._fetch_menus()

    def force_update_menu(self):
        """
        Force updates all menus.
        :return:
        """
        self.today = _get_today_as_str()
        self._fetch_menus()

    def _fetch_from(self, menu: dict, name: str):
        for period in ['Breakfast', 'Lunch', 'Dinner']:
            menu[period] = _menu(name, period, self.today)
            if menu[period] == None:
                menu[period] = {'Uh oh!': ['Something went wrong']}

    def _fetch_menus(self):
        self._fetch_from(self.brandywine, 'Brandywine')
        self._fetch_from(self.anteatery, 'The Anteatery')


def _get_today_as_str():
    return dt.today().astimezone(tz=TIMEZONE).strftime('%m/%d/%Y')


def _menu(location, period='Lunch', menu_date=_get_today_as_str()):
    return parse_menu(
        get_menu_from_campusdish_api(LOCATIONS[location], menu_date, PERIODS[period]))
