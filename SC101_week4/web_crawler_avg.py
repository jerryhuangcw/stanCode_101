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
    items = soup.find_all("td", {'class': "ratingColumn imdbRating"})
    total = 0
    count = 0
    for item in items:
        rating = float(item.strong.text)
        count += 1
        total += rating

    print('Avg(250 top rated movies):', total / count)


if __name__ == '__main__':
    main()
