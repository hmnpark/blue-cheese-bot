#from campusdish_scraper import get_menu_from_scraping
#from campusdish_scraper import BRANDY_URL, ANTEATERY_URL
from .campusdish_api import get_menu_from_campusdish_api
from .mappings import LOCATIONS, PERIODS
from .parse import parse_menu
from datetime import date

from discord_webhook import DiscordWebhook, DiscordEmbed

def sendMessageWebhook(title, description, url, color='F70D1A'):
        webhook = DiscordWebhook(url=url, username="blue cheese?")

        embed = DiscordEmbed(
                        title=title, description=description, color=color, rate_limit_retry=True
                )

        webhook.add_embed(embed)
        webhook.execute()


def get_brandy_ant_lunch():
    today = date.today().strftime('%m/%d/%Y')
    brandy_menu = parse_menu(get_menu_from_campusdish_api(LOCATIONS['Brandywine'], today, PERIODS['Lunch']))
    description = ''
    description += 'BRANDYWINE\n'
    for k,v in brandy_menu.items():
        if k == 'The Farm Stand/ Salad Bar':
            continue
        description += f'**{k}**\n'
        for item in v:
            description += f'\t{item}\n'
        description += '\n'

    description += '\n'
    ant_menu = parse_menu(get_menu_from_campusdish_api(LOCATIONS['The Anteatery'], today, PERIODS['Lunch']))
    description += 'ANTEATERY\n'
    for k,v in ant_menu.items():
        if k == "Farmer's Market":
            continue
        description += f'**{k}**\n'
        for item in v:
            description += f'\t{item}\n'
        description += '\n'
    return description

if __name__ == '__main__':
    today = date.today().strftime('%m/%d/%Y')
    # #brandy_menu = get_menu(path=Path('brandy.txt'))

    webhook_url = 'https://discord.com/api/webhooks/1028220478952853514/oikPn5gj4-1FyoBGfL28NO_K-DKo_EQmm3msMKY1ETs865JH-bP00siNhct8Kbdzd7yZ'
    sendMessageWebhook('Food!', get_brandy_ant(), webhook_url)

    print(description)

# https://uci.campusdish.com/api/menu/GetMenus?locationId=3314&storeIds=&mode=Daily&date=10/06/2022&time=&periodId=49&fulfillmentMethod=
# https://uci.campusdish.com/api/menu/GetMenus?locationId=3314&storeIds=&mode=Daily&date=10/06/2022&time=&periodId=106&fulfillmentMethod=
# https://uci.campusdish.com/api/menu/GetMenus?locationId=3314&storeIds=&mode=Daily&date=10/06/2022&time=&periodId=107&fulfillmentMethod=
# https://uci.campusdish.com/api/menu/GetMenus?locationId=3314&storeIds=&mode=Daily&date=10/06/2022&time=&periodId=108&fulfillmentMethod=

# https://uci.campusdish.com/api/menu/GetMenus?locationId=3056&storeIds=&mode=Daily&date=10/07/2022&time=&periodId=49&fulfillmentMethod=
# https://uci.campusdish.com/api/menu/GetMenus?locationId=3056&storeIds=&mode=Daily&date=10/07/2022&time=&periodId=106&fulfillmentMethod=
# https://uci.campusdish.com/api/menu/GetMenus?locationId=3056&storeIds=&mode=Daily&date=10/07/2022&time=&periodId=107&fulfillmentMethod=

# nono list: blue cheese, olive salad
