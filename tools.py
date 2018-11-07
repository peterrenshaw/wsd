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
from ast import literal_eval
from optparse import OptionParser


#======
# main: cli entry point
#======
def main():
    usage = "usage %prog -u -t"
    parser = OptionParser(usage)
    parser.add_option("-j", "--json", dest="json", 
                                      help="jsonify the data from the command line")
    parser.add_option("-p", "--pretty", action="store_true", dest="pretty", 
                                        help="make the data easier to read")
    parser.add_option("-f", "--filename", dest="filename",
                                          help="save the json data to a file")
    options, args = parser.parse_args()


    #--------
    # string to json
    #-------- 
    if options.json:
        jd = None
       
        # using the abstract syntax tree
        # to interpret py from a string  
        d = literal_eval(options.json)
      
        #---------
        # data format:
        #     convert data to json, making sure it's easy to read
        if options.pretty:
            jd  = json.dumps(d, ensure_ascii=False,
                                indent=4,
                                sort_keys=True)
        else:
            jd = json.dumps(d)

        #--------
        # save json data to file?
        if options.filename:
            fn = options.filename
            if fn:
                with open(fn, 'w') as f:
                     f.write(jd)
                f.close()
            else:
                sys.stderr.write("Error: please supply a filename.")
        else:
            print(jd)

        sys.exit(0)

    # what? display help
    else:
        parser.print_help()      
  


if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab

