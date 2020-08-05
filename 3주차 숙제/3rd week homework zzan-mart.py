from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.homework

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 아래 빈 칸('')을 채워보세요
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

rows = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for row in rows:
    rank = row.select_one(' td.number').text[0:2].strip()
    title = row.select_one('td.info > a[title]').text.strip()
    artist = row.select_one('td.info > a.artist').text
    slash = "-"
    # print(rank, title, slash, artist)

    doc = {
        'rank' : rank,
        'title' : title,
        'slash' : slash,
        'artist' : artist

    }

    db.genieChart.insert_one(doc)