#!/usr/bin/python

import sys

sales  = 0
oldKey = None
salesn = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 6:
        # Something has gone wrong. Skip this line.
        continue

    date, time, thisKey, item, thisSale, payment  = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", sales,  "\t", salesn
        oldKey = thisKey;
        sales  = 0
        salesn=0

    oldKey = thisKey
    sales  += float(thisSale)
    salesn += 1


if oldKey != None:
    print oldKey, "\t", sales, "\t", salesn

