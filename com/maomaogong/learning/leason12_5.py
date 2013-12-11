#!/usr/bin/env python

'''
Created on 11 Dec 2013

@author: t80006407

Title: Time Module
Adding Shebang on top for linux

Reference: http://docs.python.org/2/py-modindex.html
'''

print "Import Time module method 1"
import time as datetime

print "Using Time module method"
print datetime.time()
print

print "Display localtime"
print datetime.localtime()
print

print "Display more readable localtime"
print datetime.asctime()
print

print "------------------------------------------------"

print "Import Time module method 2"
from time import *

print "Using Time module method"
print time()
print

print "Display localtime"
print localtime()
print

print "Display more readable localtime"
print asctime()
print
