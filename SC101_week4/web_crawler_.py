"""
File: web_crawler_.py
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
        year = item.span.text
        if year not in d:
            d[year] = 1
        elif year in d:
            d[year] += 1

    for key, value in sorted(d.items(), key=lambda t: t[1]):
        print(key, "->", value)


if __name__ == '__main__':
    main()
