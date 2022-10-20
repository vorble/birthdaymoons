#!/usr/bin/env python3

import ephem

YEAR = 1986
MONTH = 10
DAY = 3

# Start a year early so it doesn't matter if a new or full moon happens first.
dt = ephem.Date(str(YEAR - 1) + '/' + str(MONTH) + '/' + str(DAY))
while dt < ephem.Date(str(YEAR + 120)):
    dt = ephem.next_full_moon(dt)
    dtobj = dt.datetime()
    if dtobj.month == MONTH and dtobj.day == DAY:
        print(dt, 'Full Moon')
    dt = ephem.next_new_moon(dt)
    dtobj = dt.datetime()
    if dtobj.month == MONTH and dtobj.day == DAY:
        print(dt, 'New Moon')
