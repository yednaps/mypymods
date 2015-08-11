#!/usr/bin/python

from urllib import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

outfile = "/home/sp/python/getwx/wxdata.csv"

links = {'Cha':"http://forecast.weather.gov/MapClick.php?lat=33.26893692200048&lon=-111.8117973839997",
         'Flg':"http://forecast.weather.gov/MapClick.php?lat=35.19806869600046&lon=-111.6512696319997",
         'Phx':"http://forecast.weather.gov/MapClick.php?lat=33.43416675600048&lon=-112.0080564639997",
         'Tuc':"http://forecast.weather.gov/MapClick.php?lat=32.14729897600046&lon=-110.8525860209997"}

res = {}

for c,l in sorted(links.items()):
    hl = urlopen(l).read()
    sl = BeautifulSoup(hl)
    tl = int(sl.find('p','myforecast-current-lrg').string.replace(u'\xb0F',u''))
    res[c] = tl

dt = datetime.now().strftime('%Y-%m-%d %H:%M')
data = ','.join(map(str,[t for c,t in sorted(res.items())]))

outstr = "{},{}\n".format(dt,data)

with open(outfile,'a') as f:
    f.write(outstr)
