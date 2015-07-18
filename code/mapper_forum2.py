#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re
import csv

def mapper():
	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter = '\t', quotechar='"',quoting=csv.QUOTE_NONE )
        re1 = re.compile('\W+')
	
	for line in reader:
		mydict={}
		body = line[4]
		body = body.lower()
		node = line[0]
		#print node, len(body)
		if len(body) >= 1 and node != 'id':
			body=re.sub('\N','',body)
			words = re.split(r'[\[\(:;,."-=!?\s\ )<>\]]',body)
			words1 = [x for x in words if x != '']
			for x in words1:
				if x  not in mydict:
					mydict[x] = [node]

		for x in mydict:
			print "{0}\t{1}".format(x, ''.join(mydict[x]))

def main():
        mapper()

main()


	


