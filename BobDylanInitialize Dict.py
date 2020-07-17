# BobDylan.py creates list of words from bobsyllan song bobdylan.com

import requests, bs4, pprint
from pathlib import Path
import shelve

def getWords(url):
    
    res = requests.get(url)
    res.raise_for_status()
    bobSoup =bs4.BeautifulSoup(res.text)

    lyrics = bobSoup.find("div", class_= "article-content lyrics")

    l = lyrics.getText()
    if 'Click the \'VIEW ALL\' link at the right to see a list' in l:
        return '', ''
    if l == '':
        return '', ''
    l = l.splitlines()
    l = ' '.join(l)
    l = l.expandtabs(tabsize=1)
    l = l.split(' ')
    year = ''
    words = []
    #print(len(l))
    y =[]
    for i in range(len(l)):
        if l[i] is not '':
            y.append(l[i])
   # print(y)
    for i in range(len(y)):
        x = y[i]
        x = x.rstrip(',')
        x = x.rstrip('?')
        x = x.lstrip('\'')
        x = x.rstrip('!')
        x = x.lower()
        #print(i, x)
        words.append(x)
        if x == '©':
            try:
                year = y[i+1]
            except IndexError:
                year = ''
                print('error, year not found')
            break
        if '©' in x:
            year = x.lstrip('©')
            break
    #print(words)
    if len(words) is not 0:
        del words[-1]
        del words[-1]
        return words, year
    else:
        return '', year
    
# create dictionary of urls   
res = requests.get('http://www.bobdylan.com/songs/')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
tags = soup.select('.song')
del tags[0]

songs  = {}

for i in range(len(tags)):
    link = tags[i].select('a')
    songs[str(link[0].getText())] = str(link[0].get('href'))

for key in songs:
    #print(songs[key])
    url = songs[key]
    lyrics, year = getWords(url)
    count = {}
    for word in lyrics:
        count.setdefault(word, 0)
        count[word] = count[word] + 1
    songs[key] = {}
    songs[key]['url'] =  url
    songs[key]['year'] = year
    songs[key]['words'] = count
    songs[key]['lyrics'] = lyrics
    if songs[key]['year'] == '' and songs[key]['words'] is not {}:
        print(songs[key]['url'])
hasYear = {}

for song in songs:
    if songs[song]['year'] != '':
        hasYear[song] = songs[song]
        
shelfFile = shelve.open('BobDylan')
shelfFile['songs'] = songs
shelfFile['hasYear'] = hasYear
shelfFile.close()


