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


def str2py(data):
    """
    ==== WARNING: DANGEROUS ==== 
    convert unfiltered input string from CLI to python executable code
    ==== WARNING: DANGEROUS ==== 
    """
    if data: return literal_eval(data)
    else: return None
def str2json(data, is_pretty=True, 
                   is_ensure_ascii=False,
                   is_indent=4,
                   is_sort_key=True):
    """given string data, convert to JSON with options"""
    if is_pretty:
        jd  = json.dumps(data, ensure_ascii=is_ascii,
                               indent=is_indent,
                               sort_keys=is_sort_key)
    else:
        jd = json.dumps(data)
    return jd
def build_fn(filename, ext="json", default_fn="stupid_forgot_filename"):
    """given a filename (assume valid), create a filename with extension"""
    if not filename:
        filename = default_fn
    return "{}.{}".format(filename, ext)    
def build_fpn(fp, fn):
    """
    given a filepath (will test valid) and a filename (assume valid), 
    build valid directory filepath name
    """
    if directoryname:
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
            f.write(jd)
        f.close()
        return True
    else:
        sys.stderr.write("Error: please supply a filename path.")
        sys.exit(1)

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
                                          help="supply a filename to save data to file")
    parser.add_option("-d", "--directory", dest="directory", 
                                           help="supply directory to save file")  
    options, args = parser.parse_args()


    #--------
    # string to json
    #-------- 
    if options.json:
        # using the abstract syntax tree to interpret py from a string  
        data = str2py(options.json)
      
        #---------
        # data format:
        #     convert data to json, making sure it's easy to read
        jd = str2json(data, is_pretty=options.pretty)

        #--------
        # save json data to file?
        if options.filename:
            fn = build_fn(options.filename)
            fpn = build_fpn(options.directory, fn)
            save(fpn, jd)
        else:
            print(jd)
        sys.exit(0)

    # what? display help
    else:
        parser.print_help()      
  


if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab

