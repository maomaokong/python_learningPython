#!/usr/bin/env python

'''
Created on 27 Nov 2013

@author: t80006407

Title: 6 line program sample - Import, regular expressions

Adding Shebang on top for linux
https://wiki.python.org/moin/SimplePrograms
'''

import re

for test_string in ["555-1212", "ILL-EGAL"]:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print test_string, "is a value US local phone number"
    else:
        print test_string, "rejected"