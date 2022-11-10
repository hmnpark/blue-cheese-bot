from .parse import parse_menu
from .campusdish_api import get_menu_from_campusdish_api
from .mappings import LOCATIONS, PERIODS
import datetime
from datetime import datetime as dt


TIMEZONE = datetime.timezone(-datetime.timedelta(hours=8))


class Menu:
    time: dt
    brandywine: dict
    anteatery: dict

    def __init__(self):
        self.brandywine = {'name': 'Brandywine', 'Breakfast': dict(), 'Lunch': dict(), 'Dinner': dict()}
        self.anteatery = {'name': 'The Anteatery', 'Breakfast': dict(), 'Lunch': dict(), 'Dinner': dict()}
        self._fetch_menus() # self.time is set in here

    def update_menu(self):
        if self.time != dt.date():
            self.time = dt.date()
            self._fetch_menus()

    def force_update_menu(self):
        """
        Force updates all menus.
        :return:
        """
        self._fetch_menus()

    def today_as_str(self):
        return self.time.date().strftime('%m/%d/%Y')

    def _fetch_from(self, menu: dict, name: str):
        for period in ['Breakfast', 'Lunch', 'Dinner']:
            menu[period] = _menu(name, period, self.today_as_str())
            if menu[period] == None:
                menu[period] = {'Uh oh!': ['Something went wrong']}

    def _fetch_menus(self):
        self.time = dt.today().astimezone(tz=TIMEZONE)
        self._fetch_from(self.brandywine, 'Brandywine')
        self._fetch_from(self.anteatery, 'The Anteatery')


def _menu(location, period='Lunch', menu_date=dt.today().astimezone(tz=TIMEZONE).strftime('%m/%d/%Y')):
    return parse_menu(
        get_menu_from_campusdish_api(LOCATIONS[location], menu_date, PERIODS[period]))
