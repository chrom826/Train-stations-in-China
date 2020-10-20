#coding:utf-8
import matplotlib
import matplotlib.pyplot as plt
import sqlite3

plt.rcParams['font.sans-serif']=['SimHei']

conn = sqlite3.connect('trainlist.sqlite')
cur = conn.cursor()

cur.execute('''SELECT name FROM stname WHERE longitude IS NOT NULL''')
namelist = cur.fetchall()
name = [x[0] for x in namelist]
cur.execute('''SELECT longitude FROM stname WHERE longitude IS NOT NULL''')
lnglist = cur.fetchall()
lng = [float(x[0]) for x in lnglist]
cur.execute('''SELECT latitude FROM stname WHERE longitude IS NOT NULL''')
latlist = cur.fetchall()
lat = [float(x[0]) for x in latlist]


plt.scatter(lng, lat)

for x in range(0,len(name)):
	plt.text(lng[x],lat[x],name[x],fontdict = {'size':5,'color':'black'})

plt.show()