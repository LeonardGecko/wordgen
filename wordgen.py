# MIT Licence 
# 2019 created by Reo Anzai

import random
from lxml import etree
import requests
import urllib
from bs4 import BeautifulSoup

#駅名ジェネ
def StationGen():
    line_cd = '11302'
    baseuri = 'http://www.ekidata.jp/api/l/'
    uri = baseuri + line_cd + '.xml'
    headers = {'content-type': 'text/xml'}
    response = requests.get(uri, headers=headers)
    root = etree.fromstring(response.content)

    l_station = []
    for station in root.xpath('//station'):
        l_station.append("station_name:"
        + station.findtext('station_name'))
    sta = random.choice(l_station)

    return(sta)
sta = StationGen()


#英語ジェネ
def EngGen():
    words = [line.strip() for line in open('/usr/share/dict/words')]
    eng = random.choice(words)
    return(eng)
eng = EngGen()


#英語toカタカナ
def english_to_katakana(word):
    url = 'https://www.sljfaq.org/cgi/e2k_ja.cgi'
    url_q = url + '?word=' + word
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'}

    request = urllib.request.Request(url_q, headers=headers)
    html = urllib.request.urlopen(request)
    soup = BeautifulSoup(html, 'html.parser')
    katakana_string = soup.find_all(class_='katakana-string')[0].string.replace('\n', '')

    return katakana_string
word = eng
katakana_string = english_to_katakana(word)



def WordGen():
    gen = sta + katakana_string
    return(gen)
gen = WordGen()

print(gen)
