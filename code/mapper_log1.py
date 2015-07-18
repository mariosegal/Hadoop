#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re

regex = re.compile('([(\d.)]+) ([(\D\w)+]) ([\D\w)+]) \[(.*?)\] "(.*?)" ([\d-]+) ([\d-]+)')
regex1 = re.compile('GET /[ ]?([\w\d\/\.]+)')
for line in sys.stdin:
    data = regex.match(line)
    if data != None:
    	if len(data.groups()) == 7:
        	ip, identity, user, time, url, status, size = data.groups()
        	#print "{0}\t{1}".format(url, 1)
        	page = regex1.match(url)
        	if page != None:
        		page1 = page.groups()[0] 
			print "{0}\t{1}".format(page1, '1')
