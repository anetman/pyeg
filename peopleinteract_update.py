#!/usr/bin/python3
import shelve
from person import Person
fieldnames = ('name', 'age', 'job', 'pay')
db = shelve.open('class-shelve')

while True:
	key = input('\nKey? => ')
	if not key: break
	if key in db:
		record = db[key]
	else:
		record = Person(name='?', age='?')
	for field in fieldnames:
		currval = getattr(record, field)
		newtext = input('\t[%s]=%s\n\t\tnew?=>' % (field, currval))	#you must queoto the text while you input some text
		if newtext:
			setattr(record, field, eval(newtext))
	db[key] = record
db.close()
