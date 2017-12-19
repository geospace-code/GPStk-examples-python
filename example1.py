#!/usr/bin/env python
"""
A GPSTk example with some simple time classes and functions.

This is a port of the older C++ example1.cpp.

Usage:
  python example1.py
"""
import gpstk

# In the GPSTk there are multiple classes to manage time, depending
# on the specific operation that we want to carry out. This modular
# approach eases handling the many different time systems used in the
# modern Global Navigation Satellite Systems.

# Note, however, that in the GPSTk the unifying class to do time
# Computations is the 'CommonTime' class.

# Read current time from system clock
systime = gpstk.SystemTime()

# Convert to 'CommonTime', the standard way to handle time at GPSTk
comtime = systime.toCommonTime()

# This is the typical way to handle civil time
civtime = gpstk.CivilTime(comtime)

# The YDSTime class is very useful for common GNSS tasks
ydstime = gpstk.YDSTime(comtime)

# This is a typical class to handle time in GPS system
gpstime = gpstk.GPSWeekSecond(comtime)

# Class to handle Modified Julian Date
mjd = gpstk.MJD(comtime)


print("current civil time is {}".format(civtime))
print("current year is", ydstime.year)
print("current day of year is", ydstime.doy)
print("current second of day is", ydstime.sod)
print("current full GPS week is", gpstime.week)
print("current short GPS week is", gpstime.getModWeek())
print("current day of GPS week is", gpstime.getDayOfWeek())
print("current second of GPS week is", gpstime.sow)
print("current Modified Julian Date is {}".format(mjd))
