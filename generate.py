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
DATE_UNIT = ['year', 'month', 'day', 'hour', 'minute', 'second']

#--------
# description: tools to decompose strings and build dates 
#--------
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
            sys.stderr.write("\nWarning: mmm2num Could not find mmm <{}> in {}\n".format(mmm, months))
    else:
        sys.stderr.write("\nWarning: mmm2num input failure. Could not find mmm <{}>\n".format(mmm))
def lst2int(data, start, end):
    """extract list data, convert to integer"""
    if data:
        len_d = len(data)
        # start and end inside length of data?
        if start >= 0 and start <= len_d and end >=0 and end <= len_d:
            if start >= 0 and end <= len(data):
                d = data[start:end]
                return int(d)
            else:
                sys.stderr.write("\nWarning: lst2int start and end selection invalid start <{}> end <{}>\n".format(start, end))
        else:
            sys.stderr.write("\nWarning: lst2int start<{}> and end<{}> not inside len<{}>\n".format(start, end, len_d))
    else:
        sys.stderr.write("\nWarning: lst2int has no valid input data\n")
def ex_dt(dt_str):
    """decomposition: extract date from string"""
    dtd = {}
    if is_dt_fmt(dt_str):
        # yyyymmmddThh:mm.ss 
        # 123456789012345678

        # YEAR
        year = lst2int(dt_str, 0, 4)
        if year: dtd['year'] = year

        # MONTH
        # convert string MMM to integer 00
        month = mmm2num(dt_str[4:7])
        if month >= 0 and month <= 12: dtd['month'] = month

        # DAY
        day = lst2int(dt_str, 7, 9)
        if day: dtd['day'] = day

        # HOUR
        hour = lst2int(dt_str, 10, 12)
        if hour: dtd['hour'] = hour
        
        # MINUTE
        minute = lst2int(dt_str, 13, 15)
        if minute: dtd['minute'] = minute

        # SECOND
        second = lst2int(dt_str, 16, 18)
        if second: dtd['second'] = second
        
        return dtd
    else:
        return dtd
def new_dt_delta_week(dtd):
    if 'week' in dtd: return datetime.timedelta(weeks=dtd['week'])
    else:  sys.stderr.write("\nWarning: new_dt_delta_week has no valid data <{}>\n".format(dtd))
def new_dt_delta_day(dtd):
    if 'day' in dtd: return datetime.timedelta(days=dtd['day'])
    else: sys.stderr.write("\nWarning: new_dt_delta_day has no valid data <{}>\n".format(dtd))
def new_dt_delta_hour(dtd):
    if 'hour' in dtd: return datetime.timedelta(hours=dtd['hour'])
    else: sys.stderr.write("\nWarning: new_dt_delta_hour has no valid data <{}>\n".format(dtd))
def new_dt_delta_minute(dtd):
    if 'minute' in dtd: return datetime.timedelta(minutes=dtd['minute'])
    else: sys.stderr.write("\nWarning: new_dt_delta_minute has no valid data <{}>\n".format(dtd))
def new_dt_delta_second(dtd):
    if 'second' in dtd: return datetime.timedelta(seconds=dtd['second'])
    else: sys.stderr.write("\nWarning: new_dt_delta_second has no valid data <{}>\n".format(dtd))
def create_dt(dtd):
    """given dict of date info, create a date"""
    if 'year' in dtd and 'month' in dtd and 'day' in dtd:
        return datetime.datetime(dtd['year'], dtd['month'], dtd['day'])
    else:  sys.stderr.write("\nWarning: create_dt has no valid data <{}>\n".format(dtd))
def new_delta_time(dtd):
    """given datetime, add deltatime if found"""
    dt = new_dt_delta_day(dtd)
    dt = dt + new_dt_delta_hour(dtd)
    dt = dt + new_dt_delta_minute(dtd)
    dt = dt + new_dt_delta_second(dtd)
    return dt
def is_unit(unit, units=DATE_UNIT):
    """is the datetime unit found in definition?"""
    if unit:
        if unit.lower() in units:
            return True
    return False

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

