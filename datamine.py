import json
import urllib2
import time

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


def getMatches(AccountId, region, APIKEY):
    global Players
    global Matches
    APIstring = 'https://'+region+'.api.riotgames.com/lol/match/v3/matchlists/by-account/'+AccountId+'?api_key=' + APIKEY
    try:
        data = json.load(urllib2.urlopen(APIstring))
        for matches in data['matches']:
            Matches.append(matches['gameId'])
    except urllib2.HTTPError, e:
        print "Data returned error"
        print e.code


def getPlayers(MatchID, APIKEY):
    global Players
    global Matches
    APIstring = 'https://na1.api.riotgames.com/lol/match/v3/matches/'+MatchID+'?api_key=' + APIKEY
    try:
        data = json.load(urllib2.urlopen(APIstring))
        for players in data['participantIdentities']:
            Players.append(players['player']['currentAccountId'])
    except urllib2.HTTPError, e:
        print "Data returned error"
        print e.code



Key='RGAPI-3ae5a333-a70e-4d2e-9cad-0d40910b3821'
Players = []
Matches = []

Players.append('244721782')
getMatches('244721782','na1', Key)
print "total matches",
print len(Matches)
print Matches
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
