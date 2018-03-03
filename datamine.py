import json
import urllib2
import time

def getMatches(AccountId, region, APIKEY):
    global Players
    global Matches
    APIstring = 'https://'+region+'.api.riotgames.com/lol/match/v3/matchlists/by-account/'+AccountId+'?api_key=' + APIKEY
    print APIstring
    data = json.load(urllib2.urlopen(APIstring))
    matchlist = []
    for matches in data['matches']:
        Matches.append(matches['gameId'])


def getPlayers(MatchID, APIKEY):
    APIstring = 'https://na1.api.riotgames.com/lol/match/v3/matches/'+MatchID+'?api_key=' + APIKEY

Key='RGAPI-3ae5a333-a70e-4d2e-9cad-0d40910b3821'
Players = []
Matches = []

Players.append('244721782')
getMatches('244721782','na1', Key)
print "total matches",
print len(Matches)
print Matches








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
