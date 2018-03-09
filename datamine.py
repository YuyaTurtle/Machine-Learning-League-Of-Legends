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
def BoolToBit(input):
    if (str(input).lower == 'true' or 'win'):
        return '1'
    else:
        return '0'


def AddtoFile(match):
    #15 items in teams, 4 left out since it doesnt effect the winning chance
    inputs = [0] * (16-4)
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
            f.write(inputs[x]+",")
        f.write(inputs[len(inputs)-1]+"\n")

            #if (str(x)!= 'bans' and str(x)!= 'vilemawKills' and str(x)!= 'dominionVictoryScore' ):
                #f.write(str(teams[x])+",")
        #f.write("\n\n")


def getMatches(AccountId, region, APIKEY):
    global depth
    global Players
    global Matches
    if (len(Matches) <(100000/2)):
        time.sleep(1.2)
        print "Depth: ", depth
        print "Matches: ",len(Matches)
        APIstring = 'https://'+region+'.api.riotgames.com/lol/match/v3/matchlists/by-account/'+str(AccountId)+'?api_key=' + APIKEY
        try:
            data = json.load(urllib2.urlopen(APIstring))
            temp = []
            for matches in data['matches']:
                if len(Matches) <(100000/2):
                    seen = binarySearch(Matches, matches['gameId'])
                    if seen == False:
                        #Write match result to file
                        APIstringMatch = 'https://na1.api.riotgames.com/lol/match/v3/matches/'+str(matches['gameId'])+'?api_key=' + APIKEY
                        time.sleep(1.2)
                        matchdata = json.load(urllib2.urlopen(APIstringMatch))
                        AddtoFile(matchdata)
                        #add matches to total match list
                        temp.append(matches['gameId'])
                        index = bisect.bisect_left(Matches,matches['gameId'])
                        Matches.insert(index,matches['gameId'])
                        print len(Matches)*2 , "Matches Recorded"
                else:
                    break
            for unseenmatches in temp:
                if depth > 6:
                    break
                getPlayers(unseenmatches, APIKEY)
        except urllib2.HTTPError, e:
            print "Data returned error"
            print e.code


def getPlayers(MatchID, APIKEY):
    global depth
    global Players
    global Matches
    time.sleep(1.2)
    print "Players: ",len(Players)
    APIstring = 'https://na1.api.riotgames.com/lol/match/v3/matches/'+str(MatchID)+'?api_key=' + APIKEY
    try:
        data = json.load(urllib2.urlopen(APIstring))
        #AddtoFile(data)
        for players in data['participantIdentities']:
            if binarySearch(Players, players['player']['currentAccountId']) == False:
                #Players.append(players['player']['currentAccountId'])
                index = bisect.bisect_left(Players,players['player']['currentAccountId'])
                Players.insert(index,players['player']['currentAccountId'])
                depth += 1
                getMatches(players['player']['currentAccountId'],'na1', Key)
                depth -= 1
    except urllib2.HTTPError, e:
        print "Data returned error"
        print e.code



Key='RGAPI-4cef7cf4-ef61-4587-9f68-901b06221833'
Players = []
Matches = []
depth = 0

fin= open("matchHistory.txt","w")
fin.close()

Players.append('244721782')
getMatches(244721782,'na1', Key)
print "total matches",
print len(Matches)
print Matches

print Players

#
# Matches.append('2730022598')
# getPlayers('2730022598',Key)
# print "Players in a match",
# print len(Players)
# print Players








# APIstring = "https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/244721782?endIndex=1&api_key=RGAPI-3ae5a333-a70e-4d2e-9cad-0d40910b3821"
# print json.load(urllib2.urlopen(APIstring))

#
# for i in range(999):
#     for j in range (11):
#         region = ''
#         if j == 0:
#             region = 'ru'
#         elif j == 1:
#             region = 'kr'
#         elif j == 1:
#             region = 'kr'
#         elif j == 1:
#             region = 'kr'
#         elif j == 1:
#             region = 'kr'
#         elif j == 1:
#             region = 'kr'
#         elif j == 1:
#             region = 'kr'
#
#
#         APIstring = 'https://'+region+'.api.riotgames.com/lol/match/v3/matchlists/by-account/'+str(i)+'?endIndex=1&api_key=RGAPI-3ae5a333-a70e-4d2e-9cad-0d40910b3821'
#         print APIstring
#         time.sleep(1)
#         try:
#             print "ID = " + str(i)
#             print json.load(urllib2.urlopen(APIstring))
#         except urllib2.HTTPError, e:
#             print "Data returned error"
#             print e.code
