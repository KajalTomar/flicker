#!/usr/bin/python3
import psycopg2
import time 
from datetime import datetime

conn = psycopg2.connect(
    database='data', 
    user='postgres', 
    password='Shillai1!', 
    host='127.0.0.1',
    port='5432')

# cur allows us to execute statements using cursor method
cur = conn.cursor() 

today = datetime.today()
now = datetime.now()

currentDate = today.strftime("%Y-%m-%d")
currentTime = now.strftime("%H:%M:%S")

streak = 5

SQL = "INSERT INTO streakinfo(date,streak)values(%s,%s)"

#cur.execute("CREATE TABLE streakinfo (date date PRIMARY KEY, streak smallint, time time);")
cur.execute("INSERT INTO streakinfo(date,streak)values(%s,%s)",(currentDate,streak))

conn.commit()

cur.close()
conn.close()