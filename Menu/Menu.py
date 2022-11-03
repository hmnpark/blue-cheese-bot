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

    def _fetch_menus(self):
        # TODO: what if menu fetching fails?
        temp_menu = {'Breakfast': dict(), 'Lunch': dict(), 'Dinner': dict()}

        temp_menu['Breakfast'] = _menu('The Anteatery', 'Breakfast', self.today)
        temp_menu['Lunch'] = _menu('The Anteatery', 'Lunch', self.today)
        temp_menu['Dinner'] = _menu('The Anteatery', 'Dinner', self.today)
        temp_menu['name'] = 'The Anteatery'
        self.anteatery = temp_menu

        self.brandywine['Breakfast'] = _menu('Brandywine', 'Breakfast', self.today)
        self.brandywine['Lunch'] = _menu('Brandywine', 'Lunch', self.today)
        self.brandywine['Dinner'] = _menu('Brandywine', 'Dinner', self.today)
        self.brandywine['name'] = 'Brandywine'


def _menu(location, period='Lunch', menu_date=date.today().strftime('%m/%d/%Y')):
    return parse_menu(
        get_menu_from_campusdish_api(LOCATIONS[location], menu_date, PERIODS[period]))
