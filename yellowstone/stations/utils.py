from bs4 import BeautifulSoup
from stations.models import Station

import requests


def station_list(url):

    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, "html.parser")
    station_code = []
    divs = soup.find_all("table", {"class": "zebra-striped"})

    for div in divs:
        rows = div.find_all('tr')

    station_info = []
    td_list = []

    for tr in rows:
        for td in tr.find_all('td'):
            td_list.append(td.findNext(text=True))

        station_info.append(td_list)
        td_list = []

    for i in station_info[1:]:

        station_code.append(i)
        print(i)

print(station_list("http://irfca.org/apps/station_codes"))
