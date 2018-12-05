#!/usr/bin/env python3
# ~*~ encoding: utf-8 ~*~


#========
# name: generate.py
# date: 2018NOV30
# prog: pr
# desc: generate data (at the moment Dates) so I can quickly 
#       work with known data to use in D3 understanding, testing. 
#
#       fail fast on invalid data
#
# src: <https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior>      
# optn:       
#       start:          start date in known format
#                           yyyymmmddThh:mm.ss
#       frequency:      number of data points
#                           N, integer of points 
#            
# 
#       range:		range of data from start, end
#                           [start, end]
#
#       template:       use c sprintf for template formatting
#                           '%y/%m/%d'
#
#       json            convert to JSON
#                           y/n
#       
#       WSD ☀️🌤️🌦️🌧️
#========


import os
import sys
import time
import datetime
from ast import literal_eval
from optparse import OptionParser


from tools import ex_dt
from tools import create_dt
from tools import new_delta_time
from tools import is_unit


#======
# main: cli entry point
#======
def main():
    usage = "usage %prog -u -t"
    parser = OptionParser(usage)
    parser.add_option("-s", "--start", dest="start", 
                                       help="start date to work with")
    parser.add_option("-f", "--frequency", dest="frequency", 
                                       help="number of data points from start")
    parser.add_option("-i", "--interval", dest="interval",
                                       help="sample at I interval times with U units")
    parser.add_option("-r", "--range", dest="range",
                                       help="range R of interval from start")
    parser.add_option("-u", "--unit",  dest="unit",
                                       help="unit U of I interval")
    parser.add_option("-t", "--template", dest="template",
                                       help="display show as template string using C, printf formatting")
    parser.add_option("-j", "--json",  dest="json",
                                       action="store_true",
                                       help="convert data to JSON format")
    options, args = parser.parse_args()


    if options.range and options.unit and options.interval:
        print("r=<{}> f=<{}> u=<{}> i=<{}>".format(options.range, options.frequency, options.unit, options.interval))

        # using the abstract syntax tree
        # to interpret py from a string  
        r = literal_eval(options.range)

        print("r=<{}> ({})".format(r, len(r)))
        # is length ok
        if not len(r) == 2:
            sys.stderr.write("\nError: please supply valid range: [2018, 2019]")

        # I expect two valid dates as list
        start = r[0]
        end = r[1]
        print("start <{}> end <{}>".format(start, end))
         

        if options.json:
            print("output to json")
        else:
            print("output as py")
    elif options.start and options.frequency and options.unit and options.interval:
        print("s=<{}> f=<{}> u=<{}> i=<{}>".format(options.start, options.frequency, options.unit, options.interval))

        # build data
        dtd = ex_dt(options.start)
        print("dtd=<{}>".format(dtd))

        # create start datetime
        dt = create_dt(dtd)
        print("dt=<{}>".format(dt))

        # update deltatime
        deltatime = new_delta_time(dtd)
        print("delta=<{}>".format(deltatime))

        # date plus deltatime
        dt = dt + deltatime
        print("new dt=<{}>".format(dt))

        # repeat another datetime this amount
        print("f=<{}>".format(options.frequency))
        # repeat another datetime with this deltatime
        if is_unit(options.unit):
            unit = options.unit
            print("u=<{}>".format(unit))
        else:
            sys.stderr.write("\nWarning: units cannot be determined <{}>\n".format(options.unit))
            sys.exit(1)

        
   
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

