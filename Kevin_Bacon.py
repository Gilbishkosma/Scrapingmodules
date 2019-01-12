"""
Half part of
Six degree of wikipedia.
Used to get all the links in the wiki page of Kevin Bacon.
"""
import requests
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now()) #so that it will give different number every time

def getLinks(articleUrl):
	req = requests.get("http://en.wikipedia.org" + articleUrl)
	soup = BeautifulSoup(req.text,'html.parser')
	return soup.find('div',{'id':'bodyContent'}).find_all('a',href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon") #it will store all the anchor tags found in "http://en.wikipedia.org/wiki/Kevin_Bacon"
while len(links) > 0:
	newArticle = links[random.randint(0,len(links)-1)].attrs['href'] #it will select one anchor tag from all the present anchor tags
	print(newArticle)
	links = getLinks(newArticle) #again call the getLinks with a new url.

