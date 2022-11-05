from .parse import parse_menu
from .campusdish_api import get_menu_from_campusdish_api
from .mappings import LOCATIONS, PERIODS
from datetime import date


class Menu:
    def __init__(self):
        self.today = date.today().strftime('%m/%d/%Y')
        self.brandywine = {'name': 'Brandywine', 'Breakfast': dict(), 'Lunch': dict(), 'Dinner': dict()}
        self.anteatery = {'name': 'The Anteatery', 'Breakfast': dict(), 'Lunch': dict(), 'Dinner': dict()}
        self._fetch_menus()

    def update_menu(self):
        if self.today != date.today().strftime('%m/%d/%Y'):
            self.today = date.today().strftime('%m/%d/%Y')
            self._fetch_menus()

    def force_update_menu(self):
        """
        Force updates all menus.
        :return:
        """
        self.today = date.today().strftime('%m/%d/%Y')
        self._fetch_menus()

    def _fetch_from(self, menu: dict, name: str):
        for period in ['Breakfast', 'Lunch', 'Dinner']:
            menu[period] = _menu(name, period, self.today)
            if menu[period] == None:
                menu[period] = {'Uh oh!': ['Something went wrong']}

    def _fetch_menus(self):
        self._fetch_from(self.brandywine, 'Brandywine')
        self._fetch_from(self.anteatery, 'The Anteatery')

def _menu(location, period='Lunch', menu_date=date.today().strftime('%m/%d/%Y')):
    return parse_menu(
        get_menu_from_campusdish_api(LOCATIONS[location], menu_date, PERIODS[period]))
