#!/usr/bin/env python3
# ~*~ encoding: utf-8 ~*~


#========
# name: generate.py
# date: 2018NOV30
# prog: pr
# desc: generate data (at the moment Dates) so I can quickly 
#       work with known data to use in D3 understanding, testing. 
#       
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
    parser.add_option("-r", "--range", dest="range",
                                       help="range of interval from start")
    parser.add_option("-t", "--template", dest="template",
                                       help="template string using C, printf formatting")
    parser.add_option("-j", "--json",  dest="json",
                                       action="store_true",
                                       help="convert data to JSON format")
    options, args = parser.parse_args()


    if options.range:
        # using the abstract syntax tree
        # to interpret py from a string  
        r = literal_eval(options.range)

        print("r=<{}> ({})".format(r, len(r)))
        # is length ok
        if not len(r) == 2:
            sys.stderr.write("\nError: please supply valid range: [2018, 2019]")

        # I expect two valid dates in a list
        start = r[0]
        end = r[1]
        print("start <{}> end <{}>".format(start, end))
       

        if options.json:
            print("output to json")
        else:
            print("output as py")
    elif options.start and options.frequency:
        print("s=<{}> f=<{}>".format(options.start, options.frequency))

        if options.json:
            print("output to json")
        else:
            print("output as py")
    else:
        parser.print_help()      
  


if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab

