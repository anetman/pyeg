#!/usr/bin/python3
from make_db_file import bob, sue, tom
import pickle
for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue):
	recfile = open(key + '.pkl', 'wb')
	pickle.dump(record, recfile)
	recfile.close()