from bs4 import BeautifulSoup
import requests
import time
import os

source = "http://selimtemizer.com/csci235/"

val = requests.session()
Data = val.get(source).text
bs = BeautifulSoup(Data, 'lxml')
elements = bs.find_all('a')


def parseSource():
	for each in elements:
		
		link = source + each.get('href')
		name = (each.get_text()).replace(" ", "_")
		r = requests.get(link)

		if not os.path.exists("files"):
			os.makedirs("files")

		with open("files/" + name, 'wb') as f:
			f.write(r.content)
		
		time.sleep(1)


parseSource()
print("Parsing Complete!")