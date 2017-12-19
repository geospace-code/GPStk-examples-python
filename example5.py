#!/usr/bin/env python

"""
A GPSTk example featuring some file input and processing to
create a plot with matplotlib.

Usage:

  python sem_plot.py

"""
import gpstk
from matplotlib.pyplot import figure,show


# Read in data, strict=True makes dataSets a list rather than a generator:
header, dataSets = gpstk.readSEM('data/sem_data.txt', strict=True)

# Write the data back to a different file (their contents should match):
gpstk.writeSEM('sem_data.txt.new', header, dataSets)

# Read the orbit out of the data:
orbit = dataSets[0].toAlmOrbit()  # alm orbit of first data point

austin = gpstk.Position(30, 97, 0, gpstk.Position.Geodetic)  # Austin, TX

starttime = gpstk.CommonTime()    # iterator time to start at
starttime.setTimeSystem(gpstk.TimeSystem('GPS'))
endtime = gpstk.CommonTime()  # end time, 1 day later (see below)
endtime.setTimeSystem(gpstk.TimeSystem('GPS'))
endtime.addDays(1)
#%% Step through a day, adding plot points:
d = []
el = []
for t in gpstk.times(starttime, endtime, seconds=1000):
    d.append(t.getDays())
    xvt = orbit.svXvt(t)
    location = gpstk.Position(xvt.x)
    el.append(austin.elevation(location))


# Make the plot
fig = figure()
ax = fig.gca()
ax.plot(el)
ax.set_xlabel('Time (days)')
ax.set_ylabel('Elevation (degrees)')
ax.set_title('Elevation of a GPS satellite throughout the day')
show()
