#!/usr/bin/env python

'''
Created on 11 Dec 2013

@author: t80006407

Title: List Methods
Adding Shebang on top for linux
'''

myGoals = ["defeat foes", "eat veal", "make ladies swoon"]

print myGoals
print

print "List length"
print len(myGoals)
print

print "Adding new element into the existing list"
myGoals.append("teach python")
print myGoals
print

print "Insert new element into the existing list on 4th position"
myGoals.insert(3, "brush teeth daily")
print myGoals
print

print "remove existing element from list using value"
myGoals.remove("eat veal")
print myGoals
print

