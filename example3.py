#!/usr/bin/env python

"""
1. Extract pseudorange obs 
2. compute biased multipath observation.
"""
from __future__ import print_function
from gpstk import C_MPS, GAMMA_GPS, L1_FREQ_GPS
import gpstk


rfn = gpstk.getPathData() + '/test_input_rinex2_obs_RinexObsFile.06o'

# Make a GPSTk SatID used to find a specific satellite in the data
svid = gpstk.RinexSatID(5, gpstk.SatID.systemGPS)

try:
    header, data = gpstk.readRinex3Obs(rfn, strict=True)
    print(header)

    # Loop through all the epochs and process the data for each one
    for d in data:
        # Note that d is now a Rinex3ObsData

        # Check if the PRN is in view (by searching for it)
        if d.obs.find(svid) == d.obs.end():
            print(gpstk.CivilTime(d.time), 'svid', svid, 'not in view')
        else:
            P1 = d.getObs(svid, "C1W", header).data
            P2 = d.getObs(svid, "C2W", header).data
            L1 = d.getObs(svid, "L1C", header).data
            mu = P1 - L1 * (C_MPS / L1_FREQ_GPS) - 2 * (P1 - P2) / (1 - GAMMA_GPS)
            print(gpstk.CivilTime(d.time), svid, 'biased multipath', mu)

except gpstk.InvalidRequest as e:
    print("InvalidRequest:", e)
except gpstk.Exception as e:
    print(e)
