import json
import urllib2
import time
import bisect

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]
   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   return rightmark

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found
def BoolToBit(check):
    if (check == "True"):
        #return "1"
        return "1"
    elif (check == "Win"):
        return "1"
    else:
        #return "0"
        return "0"

def getChamps(APIKEY):
    count = 0
    time.sleep(1.2)
    APIstring = 'https://na1.api.riotgames.com/lol/static-data/v3/champions?locale=en_US&dataById=true&api_key=' + APIKEY
    try:
        f=open("champs.txt","w")
        data = json.load(urllib2.urlopen(APIstring))
        #AddtoFile(data)
        for champs,info in data['data']:
            print champs,	
            print info['key']
            #f.write(str(champs) + "," + str(champs['key']) + "\n")
            count+=1
        print "Total champ count = ",
        print count
        f.close()
    except urllib2.HTTPError, e:
        print "Champ Data returned error"
        print e.code



Key='RGAPI-821ebb73-8920-478f-9da9-4f0f31bb5438'

fin= open("champs.txt","w")
fin.close()

getChamps(Key)

