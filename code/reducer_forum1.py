#!/usr/bin/python

import sys

mydict1 = {}


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    
    word, nodes  = data_mapped
    if word in mydict1:
	mydict1[word].append(nodes)
    else:
	mydict1[word] = nodes		    

for x in mydict1: 	
    print x, "\t", mydict1[x]

