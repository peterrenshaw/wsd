#!/usr/bin/env python3
# ~*~ encoding: utf-8 ~*~


#========
# name: generate.se.py
# date: 2018DEC05
#       2018NOV30
# prog: pr
# desc: generate data (at the moment Dates) so I can quickly 
#       work with known data to use in D3 understanding, testing. 
#
#       fail fast on invalid data
#
#  src: <https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior>      
# usge:
#        #       start              end             intervals   units
#        ---------------------------------------------------------------------
#        ./se.py -s yyyymmmddThh    -e yyyymmmddThh -i 30       -u m   minutes
#        
#
#        ./se.py -s yyyymmmdd       -e yyyymmmdd    -i 1        -u h   hours
#
#
#        ./se.py -s yyyymmm         -e yyyymmm      -i 2        -u d   days
#      
#
# optn:       
#       start:          start date in known format
#                           yyyymmmddThh:mm.ss
#       end:            end date in known format
# 
#       interval:       an interval in time b/w start and end dates with 
#                       a numeric value and unit.
#                           10
#
#       unit:           interval unit
#                           month      M
#                           week       w
#                           day        d 
#                           hour       h most used
#                           minute     m most used
#
#       json            convert to JSON
#                           y/n
#
#       Future
#       ------------------------------------------------------------
#       template:       use c sprintf for template formatting output
#                           '%y/%m/%d'

#       
#       WSD ☀️🌤️🌦️🌧️
#========


import os
import sys
import time
import datetime
from optparse import OptionParser


import wsd
from wsd.tools import ex_dt
from wsd.tools import create_dt
from wsd.tools import new_delta_time
from wsd.tools import is_unit


#======
# main: cli entry point
#======
def main():
    usage = "usage %prog -u -t"
    parser = OptionParser(usage)

    #-------- start date, end date --------
    parser.add_option("-s", "--start", dest="start", 
                                       help="start date to work with")
    parser.add_option("-e", "--end",   dest="frequency", 
                                       help="number of data points from start")

    #-------- time interval and units of interval --------
    parser.add_option("-i", "--interval", dest="interval",
                                       help="sample at I interval times with U units")
    parser.add_option("-u", "--unit",  dest="unit",
                                       help="unit U of I interval")

    #-------- output --------
    parser.add_option("-j", "--json",  dest="json",
                                       action="store_true",
                                       help="convert data to JSON format")
    options, args = parser.parse_args()


    if options.start and options.end and options.unit and options.interval:
        print("s=<{}> e=<{}>".format(options.start, options.end))
        print("i=<{}> u=<{}>".format(options.interval, options.unit))

   
        # output to JSON?
        if options.json:
            print("output to json")
        else:
            print("output as py")

    else:
        parser.print_help()      
  


if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab

