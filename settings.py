from datetime import datetime

FIRST_DATE = datetime(2021, 12, 30, 0, 0)
TIMEOUT = 10
DEBUG = True

BOOKING_URLS = {  # noqa
    # urls to all vaccine centers to check
    'baden': 'https://outlook.office365.com/owa/calendar/ImpfzentrumKSBBaden@impfkampagne.onmicrosoft.com/bookings/',
    'muri': 'https://outlook.office365.com/owa/calendar/ImpfzentrumMuriModerna@impfkampagne.onmicrosoft.com/bookings/',
    'aaraub': 'https://outlook.office365.com/owa/calendar/impfzentrum-aarau@impfkampagne.onmicrosoft.com/bookings/',
    'aaraua': 'https://outlook.office365.com/owa/calendar/impfzentrum-koenigsfelden@impfkampagne.onmicrosoft.com/bookings/',
}
