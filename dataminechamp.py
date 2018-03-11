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


def AddtoFile(match):
    #15 items in teams, 4 left out since it doesnt effect the winning chance
    inputs = [""] * (16-4)
    f= open("matchHistory.txt","a+")
    #f.write(str(match) + "\n\n")
    for teams in match['teams']:
        for x in teams:
            if str(x)== 'win':
                inputs[0]=BoolToBit(str(teams[x]))
            elif str(x)== 'firstDragon':
                inputs[1]=BoolToBit(str(teams[x]))
            elif str(x)== 'firstInhibitor':
                inputs[2]=BoolToBit(str(teams[x]))
            elif str(x)== 'firstRiftHerald':
                inputs[3]=BoolToBit(str(teams[x]))
            elif str(x)== 'firstBaron':
                inputs[4]=BoolToBit(str(teams[x]))
            elif str(x)== 'baronKills':
                inputs[5]=str(teams[x])
            elif str(x)== 'riftHeraldKills':
                inputs[6]=str(teams[x])
            elif str(x)== 'firstBlood':
                inputs[7]=BoolToBit(str(teams[x]))
            elif str(x)== 'firstTower':
                inputs[8]=BoolToBit(str(teams[x]))
            elif str(x)== 'inhibitorKills':
                inputs[9]=str(teams[x])
            elif str(x)== 'towerKills':
                inputs[10]=str(teams[x])
            elif str(x)== 'dragonKills':
                inputs[11]=str(teams[x])

        for x in range(len(inputs)-1):
            f.write(str(inputs[x])+",")
        f.write(inputs[len(inputs)-1]+"\n")

            #if (str(x)!= 'bans' and str(x)!= 'vilemawKills' and str(x)!= 'dominionVictoryScore' ):
                #f.write(str(teams[x])+",")
        #f.write("\n\n")


def getChamps(APIKEY):
    count = 0
    time.sleep(1.2)
    APIstring = 'https://na1.api.riotgames.com/lol/static-data/v3/champions?locale=en_US&dataById=true&api_key=' + APIKEY
    try:
        data = json.load(urllib2.urlopen(APIstring))
        #AddtoFile(data)
        for champs in data['data']:
            count+=1
        print "Total champ count = ",
        print count
    except urllib2.HTTPError, e:
        print "Champ Data returned error"
        print e.code



Key='RGAPI-821ebb73-8920-478f-9da9-4f0f31bb5438'

#fin= open("matchHistory.txt","w")
#fin.close()

getChamps(Key)

