from pathlib import Path
import pprint, shelve


shelfFile = shelve.open('BobDylan')

hasYear = shelfFile['hasYear']

years = []

for key in hasYear:
    if hasYear[key]['year'] not in years:
        years.append(hasYear[key]['year'])
        
wordsYear = {}

for year in years:
    wordsYear.setdefault(year, [])

for song in hasYear:
    for year, lyrics in wordsYear.items():
        #print(year)
        #print(hasYear[song]['year'])
        if hasYear[song]['year'] == year:
            #print(lyrics)
            #print(hasYear[song]['lyrics'])
            lyrics.append(hasYear[song]['lyrics'])
            

countYear = {}
##for year in wordsYear:
##    count = {}
##    for lyrics in wordsYear[year]:
##        print(lyrics)
##        for word in lyrics:
##            print(word)
##            count.setdefault(word, 0)
##            count[word] = count[word] + 1


for year, lyrics in wordsYear.items():
    count = {}
    for word in lyrics[0]:
        count.setdefault(word, 0)
        count[word] = count[word]+1
    countYear[year] = count
        
    
