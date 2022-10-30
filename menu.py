from .parse import parse_menu
from .campusdish_api import get_menu_from_campusdish_api
from .mappings import LOCATIONS, PERIODS
from datetime import date


class Menu:
    def __init__(self):
        self.today = date.today().strftime('%m/%d/%Y')
        self.brandywine = {'Breakfast': dict(), 'Lunch': dict(), 'Dinner': dict()}
        self.anteatery = {'Breakfast': dict(), 'Lunch': dict(), 'Dinner': dict()}
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

        temp_menu['Breakfast'] = menu('The Anteatery', 'Breakfast', self.today)
        temp_menu['Lunch'] = menu('The Anteatery', 'Lunch', self.today)
        temp_menu['Dinner'] = menu('The Anteatery', 'Dinner', self.today)
        self.anteatery = temp_menu

        self.brandywine['Breakfast'] = menu('Brandywine', 'Breakfast', self.today)
        self.brandywine['Lunch'] = menu('Brandywine', 'Lunch', self.today)
        self.brandywine['Dinner'] = menu('Brandywine', 'Dinner', self.today)


def menu(location, period='Lunch', menu_date=date.today().strftime('%m/%d/%Y')):
    return parse_menu(
        get_menu_from_campusdish_api(LOCATIONS[location], menu_date, PERIODS[period]))
