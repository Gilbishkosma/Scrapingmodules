import requests
from bs4 import BeautifulSoup

class Content:
	def __init___(self,topic,url,title,body):
		self.topic = topic
		self.url = url
		self.title = title
		self.body = body

    def print(self):
    	print("New Article found for topic:{}".format(self.topic))
    	print("Title:{}".format(self.title))
    	print("Body:{}".format(self.body))
    	print("url:{}".format(self.url))

class Website:
	 """contains info about tag of website"""
	 def __init__(self,name,url,searchUrl,resultlisting,resulturl,absoluteurl,titletag,bodytag):
	 	 self.name = name
	 	 self.url = url
	 	 self.searchUrl = searchUrl
	 	 self.resultlisting = resultlisting
         self.resulturl = resulturl
         self.absoluteurl = absoluteurl
         self.titletag = titletag
         self.bodytag = bodytag

class Crawler:
	def getPage(self,url):
		try:
		   req = requests.get(url)
        except request.exceptions.RequestException:
        	return None
        return BeautifulSoup(req.txt,'html.parser')

    def safeGet(self,soup,selector):
    	childobj = soup.select(selector)
    	if childobj is not None and len(childobj) > 0:
    		return childobj[0].get_text()
        return ""
    
    def search(self,topic,site):
    	soup = getPage(site.searchUrl + topic)
    	results = soup.select(site.resultlisting)
    	for result in results:
    		 url = result.select(site.resulturl)[0].attrs['href']
    		 if(site.absoluteurl):
    		 	 soup = self.getPage(url)
    		 else:
    		 	 soup = self.getPage(site.url + url)
    		 if soup is None:
    		 	print("something went wrong")
    		 	return None
    		 title = self.safeGet(soup,site.titletag)
    		 body = self.safeGet(soup,site.bodytag)
    		 if title != "" and body != "":
    		 	  content = Content(topic,title,body,url)
    		 	  content.print()

