# Vaccine Appointment Scraper
This is a scraper to find open vaccine appointment timeslots in Aargau (Switzerland).

## Use

### Installing

Cloning the repo...

```
git clone git@github.com:DominiqueGarmier/vaccine-appointment-scraper.git
cd vaccine-appointment-scraper
```

Installing the Python enviroment...
```
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

You will also have to install the chromedriver backend for selenium. See the [Selenium Documentation](https://selenium-python.readthedocs.io/installation.html)

### Running The Scarper

First you will have to configure `settings.py`.

- `FIRST_DATE = ...` is a `datetime.datetime` object that specifies from which date onwards you would like to scrape for appointments.
- `TIMEOUT = ...` is an `int` indication the intervall at which the website is being scraped in seconds.
- `DEBUG = ...` is a `bool`, if set to true more information will printed.
- `BOOKING_URLS = ...` is a `dict[str, str]` with name of the place and url for the booking for that specific place.

Finally you can run the script!
```
python checker.py
```

## Support for Docker

If you manage to get this running in a docker container (including the selenium webdriver) feel free to submit a pullrequest with the Dockerfile.

## [License](./LICENSE)