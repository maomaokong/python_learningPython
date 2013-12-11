#!/usr/bin/env python

'''
Created on 11 Dec 2013

@author: t80006407

Title: Function Methods
Adding Shebang on top for linux

Reference: http://docs.python.org/2/py-modindex.html
'''

print "Import Time module"
import time

print "Using Time module method"
print time.time()
print

print "Display localtime"
print time.localtime(time.time())
print

print "Display more readable localtime"
print time.asctime(time.localtime(time.time()))
print