import urllib.request
import re
site=('https://demirci.siberkuvvet.com/ye-10f852a6bbd29748eeaa9d32e8aa9c17')
kelimeDosyasi='tahminler.lst'
cook={'__cfduid':"dc60ecdbbbb24856ad36f49f7679b23451507046428","_ga":"GA1.2.10431879.1507046431","_gid":"GA1.2.730065849.1511356664","PHPSESSID":"h4h3a3acq9tagtqv43lfn8con1",'_gat':"1"}
with open(kelimeDosyasi) as f:
    tumListe=f.readlines()
for kelime in tumListe:
    kelime=kelime.replace("\n","")
    url=site+'/'+kelime
    http_kodu=urllib.request.Request(site,headers={'Cookie':"__cfduid=dc60ecdbbbb24856ad36f49f7679b23451507046428; _ga=GA1.2.10431879.1507046431; _gid=GA1.2.730065849.1511356664; PHPSESSID=h4h3a3acq9tagtqv43lfn8con1"})
    print(http_kodu)
    urllib.request.urlopen(http_kodu)
    print("buradayim")
    http_kodu=str(http_kodu.getcode())
    print(url+':'+http_kodu) 
