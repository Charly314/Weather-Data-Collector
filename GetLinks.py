# This files for get links from https://water-monitoring.information.qld.gov.au/wini/documents/telem/TP_PLUVIO.HTM
# install lxml, BeautifulSoup and requests


from bs4 import BeautifulSoup
import requests




rainfall_url = "http://water-monitoring.information.qld.gov.au/wini/documents/telem/TP_PLUVIO.HTM"

response = requests.get(rainfall_url)

data = response.text

soup = BeautifulSoup(data,'lxml')

tags = soup.find_all('a')

Link_List = []

for tag in tags:

    Link_List.append(tag.get('href'))

del Link_List[0]

print(Link_List)

for links in Link_List:
    print(links)


    #print(tag.get('href'))




