import os
from os import listdir
from os.path import isfile, join
import re
import json
import textdistance as td
from textdistance import levenshtein as lvstn
import progressbar

#constants
MAX_FILE_LEN=135


if __name__ == '__main__':
	#get current working directory
	cwd=os.getcwd()
	gtr_max_len=[]
	smallest_gtr_35=''
	test_list=[]

	bm_file="/home/john/.local/share/mcomix/bookmarks.json"

	fdir="/mnt/.d/"
	library=listdir(fdir)

	#f=open(bm_file, 'rw')
	f=open(bm_file, 'r')

	data=json.load(f)

	widgets= [ progressbar.Variable('accuracy', width=4, precision=4), ' ',
			'[', progressbar.Timer(), ']',
			 progressbar.Bar(),
			 '(', progressbar.ETA(), ')'
	]

	to_remove=[]

	#print(data[1][0])
	for i in data[1]:
		if i[0] not in library:
			to_remove.append(i)
			'''
			print('for {}'.format(i[0]))
			for j in library:
				if lvstn(i[0], j) < 20:
					print(lvstn(i[0], j), j)
			print()
			'''
	bar=progressbar.ProgressBar(max_value=len(to_remove)*len(library), widgets=widgets)
	progress=0

	for i in to_remove:
		print('for {}'.format(i[0]))
		for j in library:
			distance=lvstn(i[0], j)
			if distance < 20:
				print(distance, j)
			progress+=1
			bar.update(progress)
		print()


	f.close()
