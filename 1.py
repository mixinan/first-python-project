#!/usr/bin/env python
# -*- coding utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql.cursors
resp = urlopen("http://www.7kk.com/meinv/xinggan/new----1.html").read()
soup = BeautifulSoup(resp,"html.parser")
listUrls = soup.findAll("img",attrs={"class","lazy-img"})
for img in listUrls:
    url = img['data-original']
    txt=img.parent.next_sibling.next_sibling.string
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="wiki",
        charset="utf8mb4")
    try:
        with conn.cursor() as cursor:
            sql = "insert into tb (urlname,urlhref) values(%s,%s)"
            cursor.execute(sql,(txt,url))
            conn.commit()
    finally:
        conn.close()