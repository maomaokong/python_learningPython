'''
Created on 27 Nov 2013

@author: t80006407

Title: 3 line program sample - For loop, built-in enumerate function, new style formatting

Adding Shebang on top for linux
https://wiki.python.org/moin/SimplePrograms
'''

friends = ["john", "pat", "gary", "michael"]

for i, name in enumerate(friends):
    print "iteration {iteration} is {name}".format(iteration=(i+1), name=name)
