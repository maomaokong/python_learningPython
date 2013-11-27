#!/usr/bin/env python

'''
Created on 27 Nov 2013

@author: t80006407

Title: 8 line program sample - Command line arguments, exception handling

Adding Shebang on top for linux
https://wiki.python.org/moin/SimplePrograms
'''

# This application adds up integers in the command line

import sys

try:
    total = sum(
                int(arg)
                for arg in sys.argv[1:]
                )
    print "sum=", total
except ValueError:
    print "Please supply integer arguments"