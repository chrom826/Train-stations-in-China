#coding=utf-8
import urllib.request, urllib.parse, urllib.error
import json
import sqlite3
import re

conn = sqlite3.connect('trainlist.sqlite')
cur = conn.cursor()

baseurl = 'http://api.map.baidu.com/geocoder/v2/?ak=2ae1130ce176b453fb29e59a69b18407&callback=renderOption&output=json&address='

#cur.execute('''ALTER TABLE stname ADD longitude varchar(30)''')
#cur.execute('''ALTER TABLE stname ADD latitude varchar(30)''')

cur.execute('''SELECT name FROM stname WHERE longitude IS NULL''')
namelist = cur.fetchall()
osml = []
a = '站'
ptt = re.compile('\((.*?)\)')
for names in namelist:
	names = names[0]
	url = baseurl + urllib.parse.quote(names.encode('utf-8')) + urllib.parse.quote(a.encode('utf-8'))
	raw = urllib.request.urlopen(url)
	data = raw.read().decode()
	data = re.findall(ptt,data)[0]
	#print (type(data))
	try:
		js = json.loads(data)
	#print (type(js['status']))
	except:
		js = None
	#print(data)
	if js['status'] != 0:
		print ("retrieve failure: ", names)
		osml.append(names)
		continue

	lng = js["result"]["location"]["lng"]
	print(lng)
	lat = js["result"]["location"]["lat"]

	cur.execute('''UPDATE stname SET longitude = ? WHERE name = ?''', (lng, names))
	cur.execute('''UPDATE stname SET latitude = ? WHERE name = ?''',(lat,names))
	conn.commit()