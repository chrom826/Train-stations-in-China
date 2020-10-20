#coding=utf-8
import re
import sqlite3

conn = sqlite3.connect('trainlist.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS stname (id INTEGER PRIMARY KEY, name TEXT UNIQUE, code TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS trainlist (id INTEGER PRIMARY KEY, traincode TEXT, from_st TEXT, to_st TEXT, UNIQUE(traincode, from_st, to_st))''')

fhand = open('station_name')
fhand2 = open('train_list.js')
pattern = re.compile('\|(.*?)\|(.*?)\|.*?\|.*?\|.*?')
stations = re.findall(pattern,fhand.read())
pattern2 = re.compile('code":"(.*?)\((.*?)-(.*?)\)')
trains = re.findall(pattern2,fhand2.read())
# print (trains)
for item in stations:
	cur.execute('''INSERT OR IGNORE INTO stname (name,code) VALUES (?,?)''', (item[0], item[1]))
for item in trains:
	cur.execute('''INSERT OR IGNORE INTO trainlist (traincode, from_st, to_st) VALUES (?,?,?) ''', (item[0],item[1],item[2]))
conn.commit()