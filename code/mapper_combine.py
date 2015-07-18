#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import csv

def mapper():
	reader=csv.reader(sys.stdin,delimiter='\t')
	writer=csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_ALL)
	
	for line in reader:
		if len(line) == 5:   #we are on the users file
			if line[0] != 'user_ptr_id':
				user_ptr_id, reputation, gold, silver, bronze = line
				writer.writerow([user_ptr_id ,'A', reputation,gold,silver, bronze])
		elif len(line) == 19: 
			if line[0] != 'id':
				id= line[0]	
				title = line[1]
				tagnames = line[2]
				node_type = line[5]
				parent_id = line[6]
				abs_parent_id = line[7]
				added_at = line[8]
				author_id = line[3]
				score=line[10]
				source = 'B'
				writer.writerow([author_id, source, id,  title,  tagnames, node_type,  parent_id, abs_parent_id, added_at, score])
		else: #something weird
			continue


def main():
	mapper()


main()	
