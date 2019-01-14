import requests
from bs4 import BeautifulSoup

class Content:
	"""
	Common base class for all articles/pages
	"""
	def __init__(self,url,title,body):
		self.url = url
		self.title = title
		self.body = body
    
    def print(self):
    	print("URL : {}".format(self.url))
    	print("Title : {}".format(self.title))
    	print("Body : {}".format(self.body))

class Website:
	"""
	contains info about websites structure
	"""
	def __init__(self,name,url,titleTag,bodyTag):
		self.name = name
		self.url = url
		self.titleTag = titleTag
		self.bodyTag = bodyTag

class Crawler:

	 def getPage(self,url):
	 	try:
	 	   req = requests.get(url)
	 	except requests.exceptions.RequestException:
	 	   return None
	 	return BeautifulSoup(req.text,'html.parser')

