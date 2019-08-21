from bs4 import BeautifulSoup
import urllib.request
import requests
import time

source = "http://selimtemizer.com/csci235/"

req = urllib.request.Request(source)
resp = urllib.request.urlopen(req)
Data = resp.read()
bs = BeautifulSoup(Data, 'html.parser')


def parseSource():
	for each in bs.find_all('a'):
		link = source + each.get('href')
		name = (each.get_text()).replace(" ", "_")
		r = requests.get(link)
		with open(name, 'wb') as f:
			f.write(r.content)
		time.sleep(1)


parseSource()