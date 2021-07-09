# -*- coding: utf-8 -*-
from fastapi import FastAPI
import pymysql
from update import upd

app = FastAPI()
con = pymysql.connect(host="localhost", user="root", database="testms")


# GET return string by key
@app.get("/{word}")
async def get(word):
    cur = con.cursor()
    cur.execute("SELECT _word FROM main WHERE _key = '" + word + "'")
    res = cur.fetchall()
    if res is None:
        return "isNull"
    return res[0]


# Update db, just add to db new string
def update():
    a = upd()
    for i in a:
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO `main`(`_key`, `_word`) VALUES (%s, %s)", (i[0], i[1]))
        except:
            None
        con.commit()


update()
