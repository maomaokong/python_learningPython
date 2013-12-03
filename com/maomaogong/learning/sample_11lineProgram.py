#!/usr/bin/env python

'''
Created on 03 Dec 2013

@author: t80006407

Title: 11 line program sample - Triple-quoted strings, while loop

Adding Shebang on top for linux
https://wiki.python.org/moin/SimplePrograms
'''

REFRAIN = '''
%d bottles of beer on the wall,
%d bottles of bear,
take one down, pass it around,
%d bottles of beer on the wall!
'''

bottles_of_beer = 99

while bottles_of_beer > 1:
    print REFRAIN % (bottles_of_beer, bottles_of_beer, bottles_of_beer - 1)
    bottles_of_beer -= 1