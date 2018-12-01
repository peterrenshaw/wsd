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
def str2json(data, is_pretty):
    """given string data, convert to JSON with options"""
    # we want python structure not string
    d = str2py(data)
    if not d:
        sys.stderr.write("Error: str2json data supplied not converted using str2py.\n")
        sys.exit(1)
    else:
        if is_pretty:
           jd  = json.dumps(d, ensure_ascii=True, 
                               indent=4,
                               sort_keys=True)
        else:
           jd = json.dumps(d)

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

#======
# main: cli entry point
#======
def main():
    usage = "usage %prog -u -t"
    parser = OptionParser(usage)
    parser.add_option("-s", "--datastring", dest="datastring",
                                      help="supply data string to parse")
    parser.add_option("-j", "--json", action="store_true", dest="json", 
                                      help="jsonify the data from the command line")
    parser.add_option("-e", "--ext",  dest="ext", 
                                      help="allow for filename extension when not saving as json")
    parser.add_option("-p", "--pretty", action="store_true", dest="pretty", 
                                        help="make the data easier to read")
    parser.add_option("-f", "--filename", dest="filename",
                                          help="supply a filename to save data to file")
    parser.add_option("-d", "--dirpath", dest="dirpath", 
                                           help="supply directory to save file")  
    options, args = parser.parse_args()


    #--------
    # string to json
    #-------- 
    if options.datastring:

        #--------
        # generate data
        if options.json:
            # TODO should not have to do this
            if options.pretty: is_pretty = True
            else: is_pretty = False
            d = str2json(options.datastring, is_pretty)
        else:
            d = options.datastring
 

        #--------
        # save data to file?
        if options.filename:                
            # json? ok filename has extension 
            if options.json:
                fn = build_fn(options.filename)
            else: #not json? plz supply an ext
                if options.ext:
                    fn = build_fn(options.filename, ext=options.ext)
                else: 
                    sys.stderr.write("Error: didn't choose JSON? please supply a filename extension.")
                    sys.exit(1)

            # build fnp from fp and fn
            if options.dirpath:
                fpn = build_fpn(options.dirpath, fn)
            else:
                fpn = fn

            save(fpn, d)
        else:
            # don't specify a filename?
            # so what, redirect to a file
            print(d)

        sys.exit(0)
    else:
        #--------
        # what? can't be bothered to supply data to code, try again.
        parser.print_help()     
        sys.stderr.write("Error: no data to parse, please supply some.")
        sys.exit(1)
 
 

if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab

