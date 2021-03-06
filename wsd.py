#!/usr/bin/env python3
# ~*~ encoding: utf-8 ~*~


#========
# name: ws.py
# date: 2018NOV13
# prog: pr
# desc: grab your local BOM data & save to file, simplify data if needed
#       save as json to new (web) directory for use.
#       
#       WSD ☀️🌤️🌦️🌧️
#
#       2018NOV13
#       create option to reverse data order to compensate for data that 
#       is ordered. this is important, especially if in the case of 
#       weather data that is date ordered. Only available if you 
#       extract and simplify. Usage below.
#
#            ./ws.py -e -s -b
#       
#       the option is only available using -e and -s
#
#
#       2018NOV06
#       add rain_trace to data processing. allows weather.js to rain
#       information     
# 
#       2018NOV02
#       fix this crap:
#
#                TODO initialisation of these fields is dodgy, verify
#                add these fields to the header so we don't have problem of 
#                undefined. But we have to work with this on d3js side
#
#       reformat that local time to a ISO format so we can convert to Date in JS side 
#       the objective here is to create a datetime ISO standard, then at JS
#       side you can create a date and manipulate it.
#
#               local_date_time_full local_date_time_iso
#           ie: "20181102083000" ==> "2018-11-02T08:30:00"
# 
#       Note the key change: local_date_time_full to local_date_time_iso
#       this needs to be used JS side.
#
#       doing this allows great flexability at the d3js side where you can 
#       manipulate dates and times at high granular level for graphing.
#
#
#       2018NOV01
#       Dates in JavaScript suck bad!
# 
#       So I'm left with pre-processing the dates and while I'm at it, 
#       reduce the number of fields (supress) so the data is ONLY what
#       I need. At the moment this is:
#
#           * date in local time
#           * temperature
#
#       need to add a blank set of keys and blank values to avoid 'undefined'
#       when reading first record. is there a better way to do this? add a 
#       header? that's what got me in the first place. 
# 
#       2018OCT31
#       for extracted weather data: minor update to make unique filename
#       with date optional & replace with default until directed. 
#       Makes easier to have the same filename when calling from D3 code.
#
#
#       2018OCT30: 
#       A lost day. bugger: the file is so complex I'm having problems 
#       parsing the data in d3. one solution is to extract what I need 
#       from this file, write to another less complex file:
#
#       filename: yyyymmmdd.json
#       
#           header.refresh_message as description
#           header.name as location
#           header.ID/header.mainID as id
#           header.main_ID as mid
#       
#           data.array: array of data files from existing file
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
#       create JSON data file
#           ./ws.py -n -t 'melbourne airport' -f "json" -u http://www.bom.gov.au/fwo/IDV60801/IDV60801.94866.json
#       GET
#           ./ws.py -g
#
#
#       EXTRACT
#           ./ws.py -e 
#       rename
#           ./ws.py -e -r
#       SIMPLIFY
#           ./ws.py -e -s 
#       backwards
#           ./ws.py -e -s -b
#
#       debug
#           ./ws.py -d
#       help
#           ./ws.py -h
# uses:
#       python requests library
#========


__url__ = "https://github.com/peterrenshaw/wsd"
__email__ = "peterrenshaw@seldomlogical.com"
__author__="Peter RENSHAW"
__license__="GNU GPL 3.0"
__version__="0.2.5"
__description__="""grab your local BOM data & save to file, simplify data if needed save as json to new (web) directory for use"""


import os
import sys
import json
import time
import datetime
from optparse import OptionParser


import requests  # pip3 import requests
from requests import get


from config import PROG_NAME
from config import BASE_PATH
from config import CONF_DATA_FILE
from config import WEATHER_DATA_ALL_FN
from config import WEATHER_DATA_SIMPLE_FN
from config import WEATHER_DATA_SIMPLE_HEAD_FN


#--------- keep here ---------
VERSION = __version__
CODE_PATH = os.path.join(BASE_PATH, "py/wsd")
DEST_PATH = os.path.join(BASE_PATH, "d3")  #TODO: optional save to argument directory
CDFPN = os.path.join(CODE_PATH, CONF_DATA_FILE)
WDFPN = os.path.join(DEST_PATH, WEATHER_DATA_ALL_FN)
#--------- keep here ---------


#--------
# get_config: load config data given filepath, 
#             return format, filename and url to extract
# 
#             WARNING: convenince methods call this
#                      function. if you want more than
#                      bit of config use this method.
#           
#             * want all the config info? use this method. 
#             * want only URL? use get_config_url
# 
#--------
def get_config(filepathname=CDFPN, debug=False):
    """
    load configuration data given filepath
    then retrieve url.
    """
    # convert from JSON
    with open(filepathname, 'r') as f:
         data = json.load(f)
    f.close()
 
    if debug:
        print("load data...")
        print("key:\tvalue")
        print("--- \t------------")
        for key in data.keys():
            print("{}:\t{}".format(key, data[key]))

    # lets download resource file
    url = data['url']
    title = data['title']
    data_format = data['format']
   
    return {'url': url, 'title': title, 'format': data_format}
def get_config_url(fpn=CDFPN, debug=False):
    """convenince method for get_config"""
    url = get_config(fpn, debug)['url']
    return url        


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
    parser.add_option("-e", "--extract", dest="extract",  action="store_true", help="extract the good bits")
    parser.add_option("-s", "--simplify", dest="simplify", action="store_true", help="simplify extaction, remove unwanted data fields")
    parser.add_option("-r", "--rename", dest="rename", action="store_true", help="rename the extracted file to ^yyymmmddThh^ format")
    parser.add_option("-b", "--backwards", dest="backwards", action="store_true", help="reverse option for data collected, reverse the data order")
    options, args = parser.parse_args()


    if options.debug:
        print("{} v{}.".format(PROG_NAME, VERSION))
        print("debug on")
        print("filepath config: <{}>".format(CDFPN))
        print("filepath latest: <{}>".format(WDFPN))

    # get the latest data
    if options.get:

        # read configuration
        if os.path.isfile(CDFPN):

            # get weather data url...
            url = get_config_url(debug=options.debug)

            # request a copy of the url file, 
            # save to file so we can use it.
            with open(WDFPN, "wb") as f:
                response = get(url)
                f.write(response.content)
            f.close()

            if options.debug:
                print("saved:\t<{}>".format(wdfn))
        else:
            sys.stderr.write("Error: No configuration file, please create a new configuration data file.")

    # build a new configuration file
    elif options.new:
        
        # given URL and TITLE
        if not options.url:
            sys.stderr.write("Error: Please a valid URL for weather location data.")
        if not options.title:
            sys.stderr.write("Error: Please supply a name or descriptive title for weather location.")
        if not options.format:
            sys.stderr.write("Error: Please supply a format for the weather location data.")

        # build and save data to file as JSON
        data = {}
        data['title'] = options.title
        data['url'] = options.url
        data['format'] = options.format

        if options.debug:
            print("create configuration")
            print("<{}>".format(data))
 
        # convert to JSON, save config
        with open(CDFPN, 'w') as f:
            json.dump(data, f, 
                      ensure_ascii=False,
                      indent=4,
                      sort_keys=True)
        f.close()
        sys.exit(0)

    elif options.extract:
        if os.path.isfile(WDFPN):
            if options.debug:
                print("extract from <{}>".format(WDFPN))

            # read, load as JSON
            data = None
            with open(WDFPN) as f:
                data = f.read()
            f.close()
 
               
            # convert data from json format 
            # to PY data structures to allow 
            # easy manipulation
            pyd = json.loads(data)


            #--------
            # extract good bits:
            #     this is hard-coded for the BOM weather data
            #     formats. 
            #     
            #     WARNING: if things break, it will be here but will not be likely.  
            #   
            observations = pyd['observations']
            data = observations['data']
            header = observations['header']
            #--------


            #-------
            # data extraction:
            #     placeholder for data extraction.
            #     if options.simplify is chosen
            #         look at keys in 'key_simple' and
            #         extract and add to data list
            #     else
            #         extract all the data
            #-------
            kvd = []
            h = []
            if options.simplify:
                d = []
                ds = {}
                ds_line = {'apparent_t': 0,
                           'local_date_time_iso': '',
                           'gust_kmh': 0,
                           'rel_hum': 0,
                           'rain_trace': 0,
                           'sort_order': 0}

                # look thru data, extract keys using key_simple 
                # process, local_date_time_full
                #
                #     "20181102083000" ==> "2018-11-02T08:30:00"
                #
                # reformat that local time to a ISO format 
                # so we can convert to Date in JS side 
                title = "latest"
                name = header[0]['name']
                timezone = header[0]['state_time_zone']
                location = "{} / {}".format(name, timezone)

                message = header[0]['refresh_message']
                product = "{}.{}".format(header[0]['main_ID'], header[0]['ID'])

                #h.append(title.upper())
                h.append(location.upper())
                h.append(message.capitalize())
                #h.append(product.lower())

                # gather the data
                for item in data:
                    for key in item.keys():
                        
                        if key in ds_line:
                            ds[key] = item[key]
                        if key == 'local_date_time_full':
                            dt = datetime.datetime(*time.strptime(item['local_date_time_full'], "%Y%m%d%H%M%S")[0:5])
                            ds['local_date_time_iso'] = dt.isoformat()
                        
                    d.append(ds)
                    ds = {}
                kvd = d
            else:
                kvd = data               


            #--------
            # organise data:
            #     I want a simple list with a simple header and line items of
            #     data. A simple array in JS, header info at first line, rest
            #     of the data follows. Easy peasy. 
            data = []
            for item in kvd:        # if simple, reduced values otherwise alldata       
                data.append(item)   # lots of data items follow
            d = data
            #--------

          
            #--------
            # does the data need to be reversed?
            # this option grabs the list and 
            # reverses the order so it is backwards.
            if options.backwards:
                d.reverse()
                if options.debug:
                    print("{}\n{}\n{}".format(len(d), d[0], d[len(d)-1]))


            #--------
            # build file name:
            #     SPECIFIC (-r, rename option. takes no options formats as yyyymmmddThh
            #     I want a filename that is unique to the hour. I don't care if
            #     it's overwritten, however it may/maynot represent the ^latest^ so 
            #     remember the date as a string is in the output description.
            #     GENERIC (default)
            #     uses generic name as this is easy to call when updating
            #     using remote code
            #
            if options.rename: 
                # build unique filename: YYYY, MMM, DD, 'T' and 24HH
                fn = time.strftime("%Y%b%dT%H")
                fn = "{}.json".format(fn.upper())
                fnh = "{}-header.json".format(fn.upper())
            else:
                # different fn, dont overwrite detailed fn. 
                # use default fn for simplified, extracted data
                fn = WEATHER_DATA_SIMPLE_FN
                fnh = WEATHER_DATA_SIMPLE_HEAD_FN 

            # filepath with destination path           
            fpn = os.path.join(DEST_PATH, fn)
            fpnh = os.path.join(DEST_PATH, fnh)    
            #--------


            #---------
            # data format:
            #     convert data to json, making sure it's easy to read
            jd  = json.dumps(d, ensure_ascii=False,
                                      indent=4,
                                      sort_keys=True)
            jdh = json.dumps(h, ensure_ascii=False,
                                indent=4,
                                sort_keys=True)
            #---------


            #--------
            # save simple weather DATA file
            with open(fpn, 'w') as f:
                f.write(jd)
            f.close()
            # save simple weather HEADER file
            with open(fpnh, 'w') as f:
                f.write(jdh)
            f.close()
            #--------

            sys.exit(0)
        else:
            sys.stderr.write("Error: cannot locate file to extract")
 
    # what? display help
    else:
        parser.print_help()      
  


if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab


