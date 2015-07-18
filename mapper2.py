def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    top = []
    for line in reader:

        # YOUR CODE HERE
        body = line[4]
        #if it passes the requirements add it to the list
        if ((body[-1] == '.' or body[-1] == '!' or body[-1] == "?") and ((body.count('?')+body.count('!')+body.count('.'))==1) ) or ((body.count('?')+body.count('!')+body.count('.'))==0):
            top.append(line)

    top.sort(key = lambda s:  len(s[4]),reverse=True)
    top1 = top[-0:10]
    top1.sort(key=lambda s:  len(s[4]))
    for x in top1:
        writer.writerow(x)
