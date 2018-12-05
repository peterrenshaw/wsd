#!/usr/bin/env python3
# ~*~ encoding: utf-8 ~*~


#=======
# name: wsd.py
# date: 2018DEC01
# prog: pr
# desc: Setup script. wsd: read docs/ABOUT.txt
# usag: 
# 
#       # known to work python 3.5
#       $ python3 setup.py install
#
# reqr: Uses python requests installed to work
#======


import os
from setuptools import setup
from setuptools import find_packages


from wsd import __url__
from wsd import __email__
from wsd import __author__
from wsd import __license__
from wsd import __version__
from wsd import __description__


def read(fname):
    """read the specified file into a field, in this case description"""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name = "wsd",
      version = __version__,
      description = __description__,
      long_description=read('docs/README.md'),
      license = __license__,
      author = __author__,
      author_email = __email__,
      url = __url__,
      packages = find_packages(),
      keywords = ['data','local','weather'],
      zip_safe = True)


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
