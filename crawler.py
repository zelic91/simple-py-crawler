# -*- coding:utf-8 -*-
import urllib2
import re
from urllib2 import *
from re import *
from bs4 import BeautifulSoup

base = []
result = []

baseLink = "http://www.knorr.com.vn"

def getLinks(link):
	ret = []
	html = ""
	
	for line in urlopen(link):
		temp = findall('href="([a-zA-Z0-9/-]{2,})"', line)
		if (len(temp)>0):
			ret = ret + temp
		html = html + line
	if ('recipes' in link):
		soup = BeautifulSoup(html, 'lxml')
		search = soup.findAll(attrs={'class':compile(".*recipe-content-header.*")})
		for rep in search:
			extractText = rep.h2.text.encode('utf8')
			print "\n"+extractText+"\n"
			f = open("data.txt", "a")
			f.write(extractText+"\n")
			f.close()
			
	return ret

done = []

#init base
base = getLinks(baseLink+"/recipes")
done.append(baseLink+"/recipes")

while len(base)>0:
	link = base.pop(0)
	print "[P] "+link
	if done and (link in done):
		continue
	else:
		base = base + getLinks(baseLink+link)
	done.append(link)

print "Done"