#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import urllib
import urllib2
from bs4 import BeautifulSoup
import subprocess

def search(name):
	textToSearch = 'touhou ' + name + ' theme'
	query = urllib.quote(textToSearch)
	url = "https://www.youtube.com/results?search_query=" + query
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html, 'html.parser')

	return 'https://www.youtube.com' + soup.find(attrs={'class':'yt-uix-tile-link'})['href']



def getFromList(num):
	with open('touhoulist.txt', 'r') as f:
		charlist = f.read().splitlines()

	return charlist[num]

def main():
	argv = sys.argv[1]
	try:
		argv = int(argv)
		res = search(getFromList(argv))
	except ValueError:
		argv = str(argv)
		res = search(argv)

	print res
	raw_input('Ouvrir firefox ? [Entrer]')
	subprocess.call(['/home/ory/bin/firefox'] + [str(res)], shell=False)

if __name__=='__main__':
	main()