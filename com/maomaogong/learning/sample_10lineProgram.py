#!/usr/bin/env python

'''
Created on 29 Nov 2013

@author: t80006407

Title: 10 line program sample - Time, conditionals, from...import, for..else

Adding Shebang on top for linux
https://wiki.python.org/moin/SimplePrograms
'''

from time import localtime

activities = {
              7: "Sleeping"
              , 8: "Breakfast"
              , 9: "Commuting"
              , 13: "Working"
              , 14: "Lunch"
              , 17: "Working"
              , 18: "Commuting"
              , 20: "Dinner"
              , 22: "Resting"
              }

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    print activity_time
    print hour
    if hour <= activity_time:
        print activities[activity_time]
        print
        break
    else:
        print "Unknown, AFK or sleeping"