#!/usr/bin/python

import sys

oldKey = None
hits = 0
maxhits = 0
topkey = None

# Loop around the data

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, n1  = data_mapped

    if oldKey and oldKey != thisKey:
        #in this case we have a change, we need to define if the new total is
	#the current best
        if hits > maxhits:
		maxhits = hits
		topkey = oldKey
  	oldKey = thisKey
        hits  = 0 
	

    oldKey = thisKey
    hits  += float(n1)
 


if oldKey != None:
    print topkey, "\t", maxhits

