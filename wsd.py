#!/usr/bin/env python3
# ~*~ encoding: utf-8 ~*~


#========
# name: ws.py
# date: 2018OCT27
# prog: pr
# desc: grab your local BOM data  
#       save to file.
#
#       source file: 
#           melbourne airport 
#           <http://www.bom.gov.au/products/IDV60801/IDV60801.94866.shtml>
#
#       data file: 
#           melbourne airport 
#           <http://www.bom.gov.au/fwo/IDV60801/IDV60801.94866.json>
#                                  
# usge: 
#
#       create JSON data file
#           ./ws.py -n -t 'melbourne airport' -f "json" -u http://www.bom.gov.au/fwo/IDV60801/IDV60801.94866.json
#       get
#           ./ws.py -g
#
#       debug
#           ./ws.py -d
#       help
#           ./ws.py -h
# uses:
#       requests
#========


import os
import sys
import json
from optparse import OptionParser


import requests  # pip3 import requests
from requests import get


VERSION = "0.1"
PROG_NAME = "WEATHER STATION DATA"
BASE_PATH = "/Users/pr/work/code/"
CODE_PATH = os.path.join(BASE_PATH, "py/wsd")
DEST_PATH = os.path.join(BASE_PATH, "d3/data")
CONF_DATA_FILE = 'config.json'
WEATHER_DATA_FILE = 'latest-weather'


#======
# main: cli entry point
#======
def main():
    usage = "usage %prog -u -t"
    parser = OptionParser(usage)
    parser.add_option("-d", "--debug", dest="debug", action="store_true", help="show debug messages")
    parser.add_option("-n", "--new", dest="new", action='store_true', help="create new config file", )
    parser.add_option("-u", "--url", dest="url", help="url of weather data")
    parser.add_option("-f", "--format", dest="format", help="url data format")
    parser.add_option("-t", "--title", dest="title", help="name of weather location")
    parser.add_option("-g", "--get", dest="get", action="store_true", help="get lastest data")
    options, args = parser.parse_args()


    if options.debug:
        print("{} v{}.".format(PROG_NAME, VERSION))
        print("debug on")

    cdfpn = os.path.join(CODE_PATH, CONF_DATA_FILE)
    wdfpn = os.path.join(DEST_PATH, WEATHER_DATA_FILE)
    if options.debug:
        print("save config to <{}>".format(cdfpn))
        print("save weather to <{}>".format(wdfpn))

    # get the latest data
    if options.get:

        # read configuration
        if os.path.isfile(cdfpn):

            # convert from JSON
            with open(cdfpn, 'r') as f:
                data = json.load(f)
      
            if options.debug:
                print("load data...")
                print("key:\tvalue")
                print("--- \t------------")
                for key in data.keys():
                    print("{}:\t{}".format(key, data[key]))

            # lets download resource file
            url = data['url']
            title = data['title']
            data_format = data['format']

            # build weather data with file format...
            wdfn = "{}.{}".format(wdfpn, data_format)

            # request a copy of the url file, 
            # save to file so we can use it.
            with open(wdfn, "wb") as f:
                response = get(url)
                f.write(response.content)
           
            if options.debug:
                print("saved:\t<{}>".format(wdfn))

        else:
            print("Error: No configuration file, please create a new configuration data file.")
            sys.exit(1)

    # build a new configuration file
    elif options.new:
        
        # given URL and TITLE
        if not options.url:
            print("Error: Please a valid URL for weather location data.")
            sys.exit(1)     
        if not options.title:
            print("Error: Please supply a name or descriptive title for weather location.")
            sys.exit(1)
        if not options.format:
            print("Error: Please supply a format for the weather location data.")
            sys.exit(1)

        # build and save data to file as JSON
        data = {}

        data['title'] = options.title
        data['url'] = options.url
        data['format'] = options.format

        if options.debug:
            print("create configuration")
            print("<{}>".format(data))
            
        # convert to JSON, save config
        with open(cdfpn, 'w') as f:
            json.dump(data, f, 
                      ensure_ascii=False,
                      indent=4,
                      sort_keys=True)
        sys.exit(0)
                     
 
    # what? display help
    else:
        parser.print_help()      
  


if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab


