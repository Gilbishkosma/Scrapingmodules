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


def getInternalLinks(soup,includeUrl):
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
		print('No internalLinks')
	return internalLinks

def getExternalLinks(soup,excludeUrl):#it will not contain the url of current site
	externalLinks = []
	for link in soup.find_all('a',href=re.compile("^(http|www|https)((?!"+excludeUrl+").)*$")):
		      if link.attrs['href'] is not None:
		      	    if link.attrs['href'] not in externalLinks:
		      	    	externalLinks.append(link.attrs['href'])
	return externalLinks

def getRandomExternalLinks(startingPage):
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

def followExternalOnly(startingSite):
	externalLink = getRandomExternalLinks(startingSite)
	print(externalLink)
	followExternalOnly(externalLink)

followExternalOnly('http://oreilly.com') #starting url
