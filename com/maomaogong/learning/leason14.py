#!/usr/bin/env python

'''
Created on 11 Dec 2013

@author: t80006407

Title: Writing text to a file
Adding Shebang on top for linux

Reference: www.gutenberg.org/cache/epub/16328/pg16328.txt
'''

myText = ["I", "Love", "my", "bring", "back"]
print myText
print

print "Write content to a text file"
outfile = open("d:\desktop\output.txt", "w")
outfile.writelines(myText)
outfile.close()

