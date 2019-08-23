from bs4 import BeautifulSoup
import requests
import shutil
import os

path = "files"
source = "http://selimtemizer.com/csci235/"
info = requests.get(source).text
elements = BeautifulSoup(info, 'lxml').find_all('a')


def parseFiles():
    if not os.path.exists(path):
        os.makedirs(path)
    for each in elements:
    	tosave = path + os.sep() + each.get_text().replace(" ", "_")
        with open(tosave, 'wb') as f:
            f.write(requests.get(source + each.get('href')).content)


def zipFiles():
    parseFiles()
    where = os.path.join(os.getcwd(), path)
    shutil.make_archive(os.path.join(os.getcwd(), 'archive'), 'zip', where)
    shutil.rmtree(os.path.join(os.getcwd(), path))


userinput = input('Compress the output? Y or N:')
zipFiles() if userinput == 'Y' or userinput == 'y' else parseFiles()
print("Parsing Complete!")
