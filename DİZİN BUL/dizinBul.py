#encoding:utf-8
import requests
import itertools
import re
kelimeDosyasi='ikinciwordlist.lst'
site=('https://demirci.siberkuvvet.com/ye-10f852a6bbd29748eeaa9d32e8aa9c17')
headerss = {'host': 'demirci.siberkuvvet.com'}
cook={'__cfduid':"dc60ecdbbbb24856ad36f49f7679b23451507046428","_ga":"GA1.2.10431879.1507046431","_gid":"GA1.2.730065849.1511356664","PHPSESSID":"h4h3a3acq9tagtqv43lfn8con1",'_gat':"1"}
uzanti=[""]
a="administrator"
#site=site +'/'+ a
with open(kelimeDosyasi) as f:
    tumListe=f.readlines()
    for kelime in tumListe:
        #kelime=kelime.replace("%EXT%","")
        #kelime=kelime.replace(".%EXT%","")
        #kelime=kelime.replace(".php","")
        #kelime=kelime.replace("/","")
       # kelime=kelime.replace(".php","")
        #kelime=kelime.replace(".html","")
        #kelime=kelime.replace(".aspx","")
        #kelime=kelime.replace(".htm","")
        #kelime=kelime.replace(".asp","")
        #kelime=kelime.replace(".txt","")
	#kelime=kelime.replace(".","")
        kelime=kelime.replace("\n","")
        #print kelime
	for i in uzanti:
            if i=="":
	        url=site+'/'+kelime
		r=requests.post(url,cookies=cook)
		b=str(r)
		print(url,r)
		if b[11]=='2':
		    dosya = open('bulunanlar.lst','a')
	            dosya.write('\n')
                    dosya.write(url)
		    dosya.write('\n')
	    else:
	        url=site+'/'+kelime
	        r=requests.post(url,cookies=cook)
                b=str(r)
                print(url,r)
		if b[11]=='2':
		    dosya = open('bulunanlar.lst','a')
	            dosya.write('\n')
                    dosya.write(url)
		    dosya.write('\n')

           ## url=site+'/'+kelime+ i
	  #  r=requests.post(url,cookies=cook)
           # b=str(r)
            #if b[11]=='2':
             #  print(url,r)
	
