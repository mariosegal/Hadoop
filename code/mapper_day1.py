#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (day) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
from datetime import datetime


for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
	weekday = str(datetime.strptime(date,"%Y-%m-%d").weekday())
        print "{0}\t{1}\t{2}\t{3}".format(weekday, cost, 1,cost)

