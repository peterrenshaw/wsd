#!/usr/bin/env python3
# ~*~ encoding: utf-8 ~*~


#========
# name: config.py
# date: 2018DEC01
# prog: pr
# desc: config data. 
#       grab your local BOM data & save to file, simplify data if needed
#       save as json to new (web) directory for use.
#       
#       WSD ☀️🌤️🌦️🌧️
# uses: ast <https://docs.python.org/3.5/library/ast.html>
#========


#--------- file config ---------
PROG_NAME = "WEATHER STATION DATA (WSD)"
BASE_PATH = "/Users/pr/work/code/"
CONF_DATA_FILE = 'config.json'
WEATHER_DATA_ALL_FN = 'latest-full-weather.json'
WEATHER_DATA_SIMPLE_FN = 'latest-simple-weather.json'
WEATHER_DATA_SIMPLE_HEAD_FN = 'latest-simple-weather-header.json'    
FILENAME_DEFAULT = 'data.json'


#--------- datetime config ---------
STRF_DATE_FMT_YYYYMMMDD = "%Y%b%dT%H:%M.%S"
DATE_FORMAT_YYYYMMMDD = "YYYYMMMDDTHH:MM.SS"
DATE_MONTH = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
DATE_UNIT = ['year', 'month', 'week', 'day', 'hour', 'minute', 'second']
DATE_TIME_STORE = {'year': 1970, 'month': 1, 'day': 1, 'hour':0, 'minute':0, 'second':0.0}
STRF_DATE_FMT_DEFAULT = "%Y%M%dT%H:%M.%S"



# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab

