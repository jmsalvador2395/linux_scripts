import os
from os import listdir
from os.path import isfile, join
import re

#constants
MAX_FILE_LEN=135

'''
--------------------------
may need to use this later
--------------------------

full path + file -----> join(cwd, f)

'''

#TODO
#suggest file names for a given string
def suggest(fname):

	#use temp instead of fname for ease of readability
	temp=fname
	suggestions=[]

	#search for comiket prefixes using regex
	if re.search('\(C..\) ', fname):
		temp=fname[6:]

		if len(temp)<MAX_FILE_LEN:
			suggestions.append(temp)

	return suggestions

if __name__ == '__main__':
	cwd=os.getcwd()
	gtr_135=[]
	lsseq_135=[]
	smallest_gtr_35=''

	#create list of files that exceed 135 characters
	for f in listdir(cwd):
		potential_file=f

		if len(f) > 135:
			gtr_135.append(f)

			if smallest_gtr_35=='' or len(f)<len(smallest_gtr_35):
				smallest_gtr_35=f

	#TODO
	#go through each file to rename
	if len(gtr_135)>0:
		print(str(len(gtr_135)) + ' files to rename:\n')
		for i in gtr_135:
			suggestions=suggest(i)
			#print(str(i) + '\n')
			

		
