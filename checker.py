# standard library
import time
from datetime import datetime

# 3rd party
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as Soup
from rich.console import Console

# local imports
import settings

console = Console()


def check_if_open(driver):
    for place, url in settings.BOOKING_URLS.items():

        if settings.DEBUG:
            console.print(f'checking {place} ...', style='green')

        driver.get(url)
        time.sleep(1)

        html = driver.execute_script(
            "return document.getElementsByTagName('html')[0].innerHTML"
        )

        soup = Soup(html, "html.parser")
        open_time_slot_divs = soup.find_all("div", class_="bookable")

        dates = [
            datetime.strptime(div['data-value'], "%Y-%m-%dT%H:%M:%S.%fZ")
            for div in open_time_slot_divs
        ]  # noqa
        valid_dates = set(
            date for date in dates if date.date() >= settings.FIRST_DATE.date()
        )  # noqa

        if valid_dates or settings.DEBUG:
            console.print(
                f'dates found: {*valid_dates,} in {place}',
                style='bold red',
            )


def main():
    console.print('starting ...')
    console.print(f'checking for dates after: {settings.FIRST_DATE}')
    console.print('starting web driver ...')

    opts = Options()
    opts.add_argument("--headless")
    driver = webdriver.Chrome(options=opts)

    console.print('webdriver running ...')

    while True:
        try:
            check_if_open(driver)
        except Exception:
            console.print_exception(show_locals=True)
        if settings.DEBUG:
            console.print(f'waiting {settings.TIMEOUT}s', style='yellow')
        time.sleep(settings.TIMEOUT)


if __name__ == '__main__':
    raise SystemExit(main())
