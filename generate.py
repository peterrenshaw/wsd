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


STRF_DATE_FMT_YYYYMMMDD = "%Y%b%dT%H:%M.%S"
DATE_FORMAT_YYYYMMMDD = "YYYYMMMDDTHH:MM.SS"
DATE_MONTH = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']


def is_dt_fmt(dt, dt_format=DATE_FORMAT_YYYYMMMDD):
    """is supplied date in date format?"""
    return True
def mmm2num(mmm, months=DATE_MONTH):
    """convert str MMM/mmm/Mmm to month index"""
    if mmm:
        m = mmm.upper()
        if m in months:
            return months.index(m) + 1
        else:
            return 0
    else:
         sys.stderr.write("\nError: mmm2num input failure. Could not find mmm <{}>".format(mmm))
def lst2int(data, start, end):
    """extract list data, convert to integer"""
    if data:
        if start >= 0 and end <= len(data):
            d = data[start:end]
            return int(d)
        else:
            sys.stderr.write("\nError: lst2int start and end selection invalid start <{}> end <{}>".format(start, end))
    else:
        sys.stderr.write("\nError: lst2int has no valid input data")
def ex_dt(dt_str):
    """extract date from string"""
    dtd = {}
    if is_dt_fmt(dt_str):
        # yyyymmmddThh:mm.ss 
        # 123456789012345678
        year = lst2int(dt_str, 0, 4)
        if year: dtd['year'] = year

        # convert string MMM to integer 00
        month = mmm2num(dt_str[4:7])
        if month >= 0 and month <= 12: dtd['month'] = month

        day = lst2int(dt_str, 7, 9)
        if day: dtd['day'] = day

        hour = lst2int(dt_str, 10, 12)
        if hour: dtd['hour'] = hour
        
        minute = lst2int(dt_str, 13, 15)
        if minute: dtd['minute'] = minute

        second = lst2int(dt_str, 16, 18)
        if second: dtd['second'] = second
        
        return dtd
    else:
        return dtd
def create_dt(dtd):
    """given dict of date info, create a date"""
    
    dt = datetime.datetime(dtd['year'], dtd['month'], dtd['day'])
  
    # timedelta
    if dtd['hour']:
        h = datetime.timedelta(hours=dtd['hour'])
        dt = dt + h
        print("hour=<{}> td=<{}>".format(h, dt.hour))
    if dtd['minute']:
        m = datetime.timedelta(minutes=dtd['minute'])
        dt = dt + m
        print("minute=<{}> td=<{}>".format(m, dt.minute))
    if dtd['second']:
        s = datetime.timedelta(seconds=dtd['second'])
        dt = dt + s
        print("seconds=<{}> td=<{}>".format(s, dt.second))
        
     
    return dt    


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
    parser.add_option("-u", "--unit",  dest="unit",
                                       help="unit of interval")
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

        # I expect two valid dates as list
        start = r[0]
        end = r[1]
        print("start <{}> end <{}>".format(start, end))
         

        if options.json:
            print("output to json")
        else:
            print("output as py")
    elif options.start and options.frequency and options.unit:
        print("s=<{}> f=<{}> u=<{}>".format(options.start, options.frequency, options.unit))

        dtd = ex_dt(options.start)
        print("dtd=<{}>".format(dtd))


        dt = create_dt(dtd)
        print("dt=<{}>".format(dt))

        if options.json:
            print("output to json")
        else:
            print("output as py")

    else:
        parser.print_help()      
  


if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab

