"""
Half part of
Six degree of wikipedia.
Used to get all the links in the wiki page of Kevin Bacon.
"""
import requests
from bs4 import BeautifulSoup
import re

url = "http://en.wikipedia.org/wiki/Kevin_Bacon"

req = requests.get(url)

soup = BeautifulSoup(req.text,'html.parser')
for link in soup.find('div',id="bodyContent").find_all('a',href=re.compile("^(/wiki/)((?!:).)*$")):
	if 'href' in link.attrs:
		 print(link.attrs['href'])