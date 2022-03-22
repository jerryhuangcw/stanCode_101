"""
File: web_crawler_avg.py
Name: Jerry Huang
------------------------------
IMDB TOP RATED 250 WEB CRAWLER
"""

import requests
from bs4 import BeautifulSoup


def main():
    url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html)
    items = soup.find_all("td", {'class': "titleColumn"})
    d = {}
    for item in items:
        dir_ = item.a['title'].split(',')[0]
        dir_ = dir_[:dir_.find('(')]
        if dir_ not in d:
            d[dir_] = 1
        elif dir_ in d:
            d[dir_] += 1
    for key, value in sorted(d.items(), key=lambda e: e[1]):
        print(key, "->", value)


if __name__ == '__main__':
    main()
