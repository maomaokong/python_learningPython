#!/usr/bin/env python

'''
Created on 11 Dec 2013

@author: t80006407

Title: Reading text
Adding Shebang on top for linux

Reference: www.gutenberg.org/cache/epub/16328/pg16328.txt
'''

print "Open txt file"
book = open("d:\desktop\pg16328.txt")
print book
print

print "Read each line from book"
booktxt = book.readlines()
print

print "Show total line for this book"
print len(booktxt)
print

print "Display first 3 lines content from this book"
print booktxt[0]
print booktxt[1]
print booktxt[2]
print

print "Display first 3 line using range"
print booktxt[0:3]
print



