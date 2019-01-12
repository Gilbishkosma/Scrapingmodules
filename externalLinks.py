"""

"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import datetime
import random

pages = set() #To check the dublicacy of a url
random.seed(datetime.datetime.now())
allExtLinks = set()
allIntLinks = set()

def getInternalLinks(soup,includeUrl):#returns all internal links
	includeUrl = "{}://{}".format(urlparse(includeUrl).scheme,urlparse(includeUrl).netloc)
	internalLinks = []
	try:
		for link in soup.find('a',href=re.compile('^(/|.)*' + includeUrl )): #starting with / and can include url in between
			 if link.attrs['href'] is not None:
		 		 if link.attrs['href'] not in internalLinks:
		 	 		  if(link.attrs['href'].startswith('/')): 
		 	 	  		   internalLinks.append(includeUrl+link.attrs['href'])#make it a complete url
		 	 		  else:
		 	 	  		   internalLinks.append(link.attrs['href'])
	except:
		print('No anchor in internal')
	return internalLinks

def getExternalLinks(soup,excludeUrl):#it will not return the url of current site,return external links
	externalLinks = []
	try:
	   for link in soup.find_all('a',href=re.compile("^(http|www|https)((?!"+excludeUrl+").)*$")):
		      if link.attrs['href'] is not None:
		      	    if link.attrs['href'] not in externalLinks:
		      	    	externalLinks.append(link.attrs['href'])
	except:
		print("No anchor in external")
	return externalLinks

def getRandomExternalLinks(startingPage): #to get randomly extenal links
	req = requests.get(startingPage)
	soup = BeautifulSoup(req.text,'html.parser')
	externalLinks = getExternalLinks(soup,urlparse(startingPage).netloc)
	if len(externalLinks) == 0:
		print('No external links')
		link = "{}://{}".format(urlparse(startingPage).scheme,urlparse(startingPage).netloc)
		internalLinks = getInternalLinks(soup,link)
		if len(internalLinks) == 0:
			print('Stopping it')
			exit()
		return getRandomExternalLinks(internalLinks[random.randint(0,len(internalLinks)-1)])
	else:
		return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):#to start the getRandomlyExternallinks
	externalLink = getRandomExternalLinks(startingSite)
	print(externalLink)
	followExternalOnly(externalLink)

def getAllExternalLinks(siteUrl): #to get all external links of a page
	req = requests.get(siteUrl)
	soup = BeautifulSoup(req.text,'html.parser')
	domain = "{}://{}".format(urlparse(siteUrl).scheme,urlparse(siteUrl).netloc)
	internalLinks = getInternalLinks(soup,domain)
	externalLinks = getExternalLinks(soup,domain)

	for link in externalLinks:
		if link not in allExtLinks:
			  print(link)
			  allExtLinks.add(link)
	for link in internalLinks:
		if link not in allIntLinks:
			  allIntLinks.add(link)
			  getAllExternalLinks(link)

allExtLinks.add('http://oreilly.com')
getAllExternalLinks('http://oreilly.com')