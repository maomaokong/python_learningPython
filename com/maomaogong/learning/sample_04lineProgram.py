#!/usr/bin/env python

'''
Created on 27 Nov 2013

@author: t80006407

Title: 4 line program sample - Fibonacci, tuple assignment

Adding Shebang on top for linux
https://wiki.python.org/moin/SimplePrograms
'''

parents, babies = (1, 1)

while babies < 100:
    print "This generation has {0} babies".format(babies)
    parents, babies = (babies, parents + babies)