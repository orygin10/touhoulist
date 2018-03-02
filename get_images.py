from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import cookielib
import json

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def dl_images(query):
    character = query

    query = query.split()
    query ='+'.join(query)
    query += "+touhou"
    url="https://www.google.com/search?q="+query+"&source=lnms&tbm=isch"
    print url
    #add the directory for your image here
    DIR="Pictures"
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
    }
    soup = get_soup(url,header)


    ActualImages=[]# contains the link for Large original images, type of  image
    for a in soup.find_all("div",{"class":"rg_meta"}):
        link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
        ActualImages.append((link,Type))

    print  "there are total" , len(ActualImages),"images"

    if not os.path.exists(DIR):
                os.mkdir(DIR)
    DIR = os.path.join(DIR, character)

    if not os.path.exists(DIR):
                os.mkdir(DIR)
    ###print images
    for i , (img , Type) in enumerate( ActualImages):
        try:
            req = urllib2.Request(img, headers={'User-Agent' : header})
            raw_img = urllib2.urlopen(req).read()

            cntr = len([i for i in os.listdir(DIR) if character in i]) + 1
            print cntr
            if len(Type)==0:
                f = open(os.path.join(DIR , character + "_"+ str(cntr)+".jpg"), 'wb')
            else :
                f = open(os.path.join(DIR , character + "_"+ str(cntr)+"."+Type), 'wb')

            f.write(raw_img)
            f.close()
        except Exception as e:
            print "could not load : "+img
            print e

with open('touhoulist.txt', 'r') as f:
    charlist = f.read().splitlines()

for char in charlist:
    dl_images(char)