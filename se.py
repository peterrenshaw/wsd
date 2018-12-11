#!/usr/bin/env python3
# ~*~ encoding: utf-8 ~*~


#========
# name: se.py
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
#       format:         use c sprintf from config for template formatting output
#                           '%y/%m/%d'
#
#       
#       WSD ☀️🌤️🌦️🌧️
#========


import os
import sys
import time
import datetime
from optparse import OptionParser


from tools import ex_dt
from tools import save
from tools import py2json
from tools import is_unit
from tools import dt_new_date
from tools import dt_new_delta


from config import IS_DEBUG
from config import FILENAME_DEFAULT
from config import STRF_DATE_FMT_DEFAULT


#======
# main: cli entry point
#======
def main():
    usage = "usage %prog -s -e -i -u -f -j"
    parser = OptionParser(usage)

    #-------- start date, end date --------
    parser.add_option("-s", "--start", dest="start", 
                                       help="start date to work with")
    parser.add_option("-e", "--end",   dest="end", 
                                       help="number of data points from start")

    #-------- time interval and units of interval --------
    parser.add_option("-i", "--interval", dest="interval",
                                       help="sample at I interval times with U units")
    parser.add_option("-u", "--unit",  dest="unit",
                                       help="unit U of I interval")

    #-------- output --------
    parser.add_option("-f", "--format",dest="format",
                                       help="format datetime output using printf")
    parser.add_option("-j", "--json",  dest="json",
                                       action="store_true",
                                       help="convert data to JSON format")
    parser.add_option("-d", "--debug", dest="debug",
                                       action="store_true",
                                       help="display debug messages")
    options, args = parser.parse_args()

   
    if options.debug:
        is_debug = True
    else:
        is_debug = IS_DEBUG


    if options.start and options.end and options.unit and options.interval:
        # break down dt from string input
        # create start date, end date
        start = dt_new_date(ex_dt(options.start))
        end =  dt_new_date(ex_dt(options.end))

        # create a new datetime delta OR fail
        d = dt_new_delta(options.interval, options.unit)

        if is_debug:
            print("start dt={}".format(start))
            print("end   dt={}".format(end))
            print("d     dt={}".format(d))

        # formatting output OR use option default?
        if options.format:
            dtf = options.format
        else: 
            dtf = STRF_DATE_FMT_DEFAULT

        # store result, set var for current date time
        t = []
        cdt = start
        if is_debug:
            print("cdt   dt={}".format(cdt))
            print("cdt<=end {}".format(cdt <= end))

        # loop incrementing DELTA and add to time
        # break on current datetime <= end time
        # TODO no internal short circuit
        while cdt <= end:

            t.append(cdt.strftime(dtf))
            cdt = cdt + d

        # output to JSON or console?
        if options.json:
            dj = py2json(t)
            save(FILENAME_DEFAULT, dj)
        else:
            for item in t:
                print(item)

    else:
        parser.print_help()      
  


if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab

