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
	mydict = {}
	for line in reader:
		body = line[4]
		body = body.lower()
		node = line[0]
		#print node, len(body)
		if len(body) >= 1 and node != 'id':
			#print node, body
			#p1 =(body[-1]=='.' or body[-1]=='!' or body[-1]=='?') and (body.count('?')+body.count('!')+body.count('.'))==1
			#p2=(body.count('?')+body.count('!')+body.count('.'))==0		
			#if p1 or p2:	
			body=re.sub('\N','',body)
			words = re.split('\W+',body)
			#print words
			for x in words:
				if x in mydict:
					if node not in mydict[x]:
						mydict[x].append(node)
				else:
					mydict[x] = [node]

	for x in mydict:
		print "{0}\t{1}".format(x, mydict[x])
#test_text =""\"123"\t\" "\t\"xx"\t\"rf"\t\"uno dos, tres, tres! dos? tres" ""
#print test_text

def main():
#	import StringIO
#	sys.stdin = StringIO.StringIO(test_text)
#	sys.stdin = sys.__stdin__
        mapper()

main()


	

#for line in sys.stdin:
#    data = line.strip().split("\t")
#    if len(data) == 6:
#        date, time, store, item, cost, payment = data
#        print "{0}\t{1}".format(store, cost)

