#!/usr/bin/env python

'''
Created on 27 Nov 2013

@author: t80006407

Title: 7 line program sample - Dictionaries, generator expressions

Adding Shebang on top for linux
https://wiki.python.org/moin/SimplePrograms
'''

prices = {
          "apple":0.40
          , "banana":0.50
          }

my_purchase = {
               "apple":1
               , "banana":6
               }

grocery_bill = sum(
                   prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase
                   )

print "I owe the grocer $%.2f" % grocery_bill