# -*- coding: utf-8 -*-
from docxtpl import *

import sqlite3
conn = sqlite3.connect('example.sqlite')
c = conn.cursor()
c.execute("SELECT * FROM example")
data = c.fetchall()

#get some colums
colum_names = list(map(lambda x: x[0], c.description))
rows = {}
how_much = 0
for name in colum_names:
	rows[how_much] = name
	how_much+=1

c.execute("SELECT COUNT(*) FROM users")
count = c.fetchall()
hey = 0
for cv in count:
	hey = cv[0]	
context={}

hey+=1

for o in range(1,int(hey)):
	c.execute("SELECT * FROM example WHERE ROWID=?",[o])
	print('loop: ', o)
	data = c.fetchall()
	doto = {}
	zero = 0
	for x in data:
		for i in range(0, how_much):
			doto[i] = x[i]
		for i in range(0, how_much):
			context[colum_names[int(i)]] = doto[int(i)]

		tpl = DocxTemplate("template/example_tpl.docx")
		tpl.render(context)
		tpl.save("save/"+str(o)+".docx")
