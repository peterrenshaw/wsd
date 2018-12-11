#!/usr/bin/env python3
# ~*~ encoding: utf-8 ~*~


#========
# name: tools.py
# date: 2018NOV07
# prog: pr
# desc: grab your local BOM data & save to file, simplify data if needed
#       save as json to new (web) directory for use.
#       
#       WSD ☀️🌤️🌦️🌧️
# uses: ast <https://docs.python.org/3.5/library/ast.html>
#========


import os
import sys
import json
import datetime
from ast import literal_eval
from optparse import OptionParser


from config import IS_DEBUG
from config import DATE_MONTH
from config import DATE_UNIT_DT
from config import DATE_FORMAT_YYYYMMMDD
from config import STRF_DATE_FMT_YYYYMMMDD
from config import DATE_TIME_STORE


#--------
# description: tools to decompose strings and build dates 
#--------
def dt_new_delta(interval, unit, is_debug=IS_DEBUG):
    """create a new datetime delta"""
    if interval:       
        week = 0
        day = 0
        hour = 0
        minute = 0
        second = 0

        unit = unit.lower()
        if unit ==  'd':
            day = int(interval)
        elif unit == 'h':
            hour = int(interval)
        elif unit == 'm':
            minute = int(interval)
        elif unit == 's':
            second = float(interval)
        elif unit == 'w':
            week = int(interval)
        else:
            sys.stderr.write("\nError: dt_new_delta did not supply valid unit <{}>\n".format(unit))
            sys.exit(1)

        d = datetime.timedelta(seconds=second,
                               minutes=minute, 
                               hours=hour,
                               days=day,
                               weeks=week) 

        if is_debug: 
            print("dt_new_delta: delta=<{}>".format(d))
        return d
    else:
        sys.stderr.write("\nError: dt_new_delta did not supply an interval <{}>\n".format(interval))
        sys.exit(1)
def dt_new_date(data, is_debug=IS_DEBUG):
    """given dict of date, build a new date"""
    if is_debug:
        print("dt_new_date: data=<{}>".format(data))
    dt = datetime.datetime(data['year'],data['month'],data['day'],data['hour'],data['minute'],data['second'])
    return  dt
def is_dt_fmt(dt, dt_format=DATE_FORMAT_YYYYMMMDD):
    """is supplied date in date format?"""
    return True
def mmm2num(mmm, months=DATE_MONTH, is_debug=IS_DEBUG):
    """convert str MMM/mmm/Mmm to month index"""
    if mmm:
        m = mmm.upper()
        if m in months:
            return months.index(m) + 1
        else:
            if is_debug: 
                sys.stderr.write("\nWarning: mmm2num Could not find mmm <{}> in {}\n".format(mmm, months))
    else:
        if is_debug: 
            sys.stderr.write("\nWarning: mmm2num input failure. Could not find mmm <{}>\n".format(mmm))
def lst2int(data, start, end, is_debug=IS_DEBUG):
    """extract list data, convert to integer"""
    if data:
        len_d = len(data)
        # start and end inside length of data?
        if start >= 0 and start <= len_d and end >=0 and end <= len_d:
            if start >= 0 and end <= len(data):
                d = data[start:end]
                return int(d)
            else:
                if is_debug: 
                    sys.stderr.write("\nWarning: lst2int start and end selection invalid start <{}> end <{}>\n".format(start, end))
        else:
            if is_debug: 
                sys.stderr.write("\nWarning: lst2int start<{}> and end<{}> not inside len<{}>\n".format(start, end, len_d))
    else:
        sys.stderr.write("\nWarning: lst2int has no valid input data\n")
def ex_dt(dt_str, is_debug=IS_DEBUG):
    """decomposition: extract date from string"""
    dtd={}
    if is_debug:
        print("ex_dt = {}".format(dt_str))
        print("is_dt_fmt({})={}".format(dt_str, is_dt_fmt(dt_str)))

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
        else: dtd['hour'] = 0
        
        # MINUTE
        minute = lst2int(dt_str, 13, 15)
        if minute: dtd['minute'] = minute
        else: dtd['minute'] = 0

        # SECOND
        second = lst2int(dt_str, 16, 18)
        if second: dtd['second'] = second
        else: dtd['second'] = 0

        if is_debug:
            print("dtd=<{}>".format(dtd))
        return dtd 
    else:
        sys.stderr.write("\nError: ex_dt cannot break down supplied date <{}>\n".format(dtd))
        sys.exit(1)

def is_unit(unit, units=DATE_UNIT_DT):
    """is the datetime unit found in the datetime definition?"""
    if unit:
        if unit.lower() in units:
            return True
    return False

#--------
# description: file tools
#--------
def str2py(data):
    """
    ==== WARNING: DANGEROUS ==== 
    convert unfiltered input string from CLI to python executable code
    documentation suggests otherwise, does this work against malicious users?
    <https://docs.python.org/3/library/ast.html?highlight=ast#ast.literal_eval>
    ==== WARNING: DANGEROUS ==== 
    """
    if data:
        try: 
            pd = literal_eval(data)
        except SyntaxError as err:
            sys.stderr.write("Syntax Error: str2py data supplied not converted using str2py.\nError is <{}>\n".format(err))
            sys.stderr.write("Warning: <{}>\n".format(data))
            sys.stderr.write("Suggestion: error in string supplied needs to be corrected and valid.\n")
            sys.exit(1)
        else:
            pass
        return pd
    else:
        return None
def py2json(data, is_pretty=True):
    """convert py structure to json"""
    if is_pretty:
        jd  = json.dumps(data, 
                         ensure_ascii=True, 
                         indent=4,
                         sort_keys=True)
    else:
       jd = json.dumps(data)
    return jd

def str2json(data, is_pretty):
    """given string data, convert to JSON with options"""
    # we want python structure not string
    d = str2py(data)
    if not d:
        sys.stderr.write("Error: str2json data supplied not converted using str2py.\n")
        sys.exit(1)
    else:
        if is_pretty:
           jd  = py2json(d, is_pretty=True)
        else:
           jd = py2json(d, is_pretty=False)

        return jd
def build_ext(ext, default="txt"):
    """build 3 letter ext without dots"""
    if len(ext) == 3: return ext.lower()
    else: return default.lower()
def build_fn(filename, ext="json", default_fn="stupid_forgot_filename"):
    """given a filename (assume valid), create a filename with extension"""
    if not filename:
        filename = default_fn
    return "{}.{}".format(filename, ext)    
def build_fpn(fp, fn):
    """
    given a filepath (will test valid) and a filename (assume valid), 
    build valid directory file path name
    """
    if fp:
        if os.path.isdir(fp):
            fpn = os.path.join(fp, fn)
        else:
            sys.stderr.write("Error: please supply a valid directory file path.\n\t<{}>".format(fp))
            sys.exit(1)
    else:
        fpn = fn
    return fpn
def save(fpn, data):
    """given valid filepathname and data, save to file"""
    if fpn: # assume valid, pre-tested
        with open(fpn, 'w') as f:
            f.write(data)
        f.close()
        return True
    else:
        sys.stderr.write("Error: please supply a filename path.")
        sys.exit(1)
#-------- File tools --------


#======
# main: cli entry point
#======
def main():
    sys.exit(0)

if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab

