#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 12:39:57 2018

@author: msh
"""

from astcalc import time

astime = time.astronomic(verb=False)

print("DUSK Twilights:")
print("Next DUSK Twilight Start time is: {}".format(
        astime.n_dusk_twilight_start()))
print("Next DUSK Twilight End time is: {}".format(
        astime.n_dusk_twilight_end()))
print("Previous DUSK Twilight Start time is: {}".format(
        astime.p_dusk_twilight_start()))
print("Previous DUSK Twilight End time is: {}".format(
        astime.p_dusk_twilight_end()))
print("")
print("DAWN Twilights:")
print("Next DAWN Twilight Start time is: {}".format(
        astime.n_dawn_twilight_start()))
print("Next DAWN Twilight End time is: {}".format(
        astime.n_dawn_twilight_end()))
print("Previous DAWN Twilight Start time is: {}".format(
        astime.p_dawn_twilight_start()))
print("Previous DAWN Twilight End time is: {}".format(
        astime.p_dawn_twilight_end()))
print("")
print("Moon set and rise:")
print("Next Moon Rise time is: {}".format(astime.m_nrising()))
print("Next Moon Set time is: {}".format(astime.m_nsetting()))
print("Previous Moon Rise time is: {}".format(astime.m_prising()))
print("Previous Moon Set time is: {}".format(astime.m_psetting()))
print("")
print("Sunset and Sunrise")
print("Next Sunrise time is: {}".format(astime.nrising()))
print("Next Sunset time is: {}".format(astime.nsetting()))
print("Previous Sunrise time is: {}".format(astime.prising()))
print("Previous Sunset time is: {}".format(astime.psetting()))