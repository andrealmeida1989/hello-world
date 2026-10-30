#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

count = None
sender = dict()
mutable = None
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    content = None
    content = line.split()
    if line.startswith("From") and len(content)>2:
        mutable = content[5]
        mutable = mutable[0:2]
        sender[mutable] = sender.get(mutable,0) + 1
        line = None
    else:
        continue
sortedlist = list()
for key, val in sender.items():
    newtup = (key,val)
    sortedlist.append(newtup)
sortedlist.sort()
for I in sortedlist:
    print(I[0],I[1])
#print( sorted( [ (v,k) for v,k in sender.items()]))