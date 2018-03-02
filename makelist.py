#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2

response = urllib2.urlopen("http://touhou.wikia.com/wiki/Character_List")
html = response.read()

soup = BeautifulSoup(html, 'html.parser')



for el in soup.select('a[href*="/wiki/"]'):
	if el.has_attr('title'):
		print el.get('title')