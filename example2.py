#!/usr/bin/env python
"""
A GPSTk example with some simple time classes and functions.

This is a semi-port of the older C++ example2.cpp. The original
only imported and rewrote the same file. But that would be
completely trivial for python.

Usage:
  python example2.py
"""
from __future__ import print_function
import gpstk

# Read in the rinex data
# rfn = 'data/rinex3obs_data.txt'
rfn = gpstk.getPathData() + "/test_input_rinex2_obs_RinexObsFile.06o"
header, data = gpstk.readRinex3Obs(rfn, strict=True)

# Let's pretend we want to change something in the header
# (otherwise this would be a two-line example!)
header.receiverOffset = 47

# Now let's find the earliest and latest observations
# function for how to compare Rinex3ObsData objects for min/max functions:


def timeFunction(self):
    return self.time


earliest = min(data, key=timeFunction)
latest = max(data, key=timeFunction)

print("Earliest time found:", gpstk.CivilTime(earliest.time))
print("Latest time found:", gpstk.CivilTime(latest.time))

# Now let's write it all back to a different file
gpstk.writeRinex3Obs(rfn + ".new", header, data)
