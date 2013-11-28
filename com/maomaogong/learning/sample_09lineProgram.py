#!/usr/bin/env python

'''
Created on 28 Nov 2013

@author: t80006407

Title: 9 line program sample - Opening file

Adding Shebang on top for linux
https://wiki.python.org/moin/SimplePrograms
'''

# Indent your Python code to put into an email
import glob

# glob supports Unix style pathname extension
python_files = glob.glob("*.py")

for file_name in sorted(python_files):
    print "    ------" + file_name
    
    with open(file_name) as f:
        for line in f:
            print "    " + line.rstrip()
            
    print
    raw_input()