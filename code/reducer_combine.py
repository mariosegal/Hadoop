#!/usr/bin/python

import sys
import csv



# Loop around the data
# since it is sorted the A record comes first, identify it and readit
# then read the next one, it has ot be a B or perhaps none (but that would be weird)
# then output merged data
# you cna hve one to many so keep going until the keys do not match
#only print when keys match
def reducer():
        reader=csv.reader(sys.stdin,delimiter='\t',quotechar='"')
        writer=csv.writer(sys.stdout,delimiter='\t',quotechar='"')

	
	user =0 
	post = 0
	for line in reader:
    		data_mapped = line
		
		#print len(data_mapped), data_mapped[1]
    		if  data_mapped[1]=='A' :
                        user_ptr_id ,source, reputation,gold,silver, bronze = data_mapped
                        user = 1;
                        #print user_ptr_id ,source, reputation,gold,silver, bronze;
                if data_mapped[1]=='B' :
                        author_id, source, id,  title,  tagnames, node_type,  parent_id, abs_parent_id, added_at, score = data_mapped
                        post = 1;
                        #print 'post=',post

		#if len(data_mapped) != 6 and  len(data_mapped) != 10 :
        	# Something has gone wrong. Skip this line.
        	#	continue
    		
		if user == 1 and post == 1 and author_id == user_ptr_id:
		#we have a match and both pieces so we can print the output
			writer.writerow([id, title, tagnames, user_ptr_id, node_type, parent_id, abs_parent_id, added_at, score,  reputation, gold, silver, gold]) 
			post=0  #for safety set the post as 0 as we outputted this post	




def main():
	reducer()

main()
