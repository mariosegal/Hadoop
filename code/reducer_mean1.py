#!/usr/bin/python

import sys

sales  = 0
oldKey = None
n = 0
mean1 = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) < 3 or len(data_mapped) >4 :
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale, thisN, x  = data_mapped

    if oldKey and oldKey != thisKey:
	mean1 = sales/n
	print "{0}\t{1}\t{2}\t{3}".format(oldKey, sales, n,mean1)
	#print oldKey, "\t", sales, "\t" , n, '\t', mean1
        oldKey = thisKey;
        sales  = 0
        n=0
	mean1 =0 

    oldKey = thisKey
    sales  += float(thisSale)  
    n += float(thisN)
 


if oldKey != None:
    mean1 = sales/n
    print "{0}\t{1}\t{2}\t{3}".format(oldKey, sales, n,mean1)
    #print oldKey, "\t", sales, '\t', n, '\t' , mean1
