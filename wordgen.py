from lxml import etree
import random
import requests

line_cd = '11302'
baseuri='http://www.ekidata.jp/api/l/'
uri = baseuri + line_cd + '.xml'
headers = {'content-type': 'text/xml'}
response = requests.get(
  uri,
  headers=headers)
root = etree.fromstring(response.content)

l_station = []
for station in root.xpath('//station'):
    #l_station = station.findtext('station_name')
    l_station.append("station_name:"+station.findtext('station_name'))
print(l_station)
s = random.choice(l_station);
print(s)
#  print("station_cd:"+station.findtext('station_cd'))
#  print("station_name:"+station.findtext('station_name'))
#  print("longitude:"+station.findtext('lon'))
#  print("latitude:"+station.findtext('lat'))
#  print("----------")
