from bs4 import BeautifulSoup
import requests
import shutil
import time
import os

path = "files"
source = "http://selimtemizer.com/csci235/"
info = requests.session().get(source).text
elements = BeautifulSoup(info, 'lxml').find_all('a')


def parseFiles():
    for each in elements:
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path + '/' + each.get_text().replace(" ", "_"), 'wb') as f:
            f.write(requests.get(source + each.get('href')).content)
        time.sleep(1)


def zipFiles():
    parseFiles()
    where = os.path.join(os.getcwd(), path)
    shutil.make_archive(os.path.join(os.getcwd(), 'archive'), 'zip', where)
    shutil.rmtree(os.path.join(os.getcwd(), path))


print("Compress the files into a .zip folder? Y or N:")
if(input() == 'Y' or 'y'):
    zipFiles()
else:
    parseFiles()
print("Parsing Complete!")
