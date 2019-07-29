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

#suggest file names for a given string
def suggest(fname):

	file_ext=fname[fname.rfind('.'):]
	fname_no_ext=fname[:fname.rfind('.')]
	#use temp instead of fname to avoid confusion
	suggestions=[]
	temp=fname_no_ext

	#search for and remove comiket prefixes
	#'..' has numbers in it so i may need to update it if they ever start using more digits
	if re.search('\(C..\) ', fname):
		temp=fname_no_ext[6:]
		'''
		if len(temp)<MAX_FILE_LEN:
			suggestions.append(temp)
		'''

	#serach for and remove '(COMIC....)' text
	#'....' has numbers in it so i may need to update it if they ever start using more digits
	if re.search('\(COMIC....\)', temp):
		temp=fname_no_ext[12:]

	#remove substrings beginning and ending with curly brackets
	curly_brackets=re.findall('\{.*\}', temp)
	for i in curly_brackets:
		temp=temp.replace(i, '').strip()
	
	#remove substrings beginning and ending with square brackets
	#except for author names
	square_brackets=re.findall('\[.*?\]', temp)
	print(str(len(square_brackets)) +' '+ temp + '\n')

	#if the first character in the file name is '[' then i remove
	#the first element of square_brackets from the list because 
	#that particular instance is the author
	if temp[0] == '[':
		square_brackets.pop(0)
	for i in square_brackets:
		temp=temp.replace(i, '').strip()

	#TODO
	print(temp)
	#print(temp.replace('   ', ' ')
	print(' '.join(temp.split()))
	print('\n')
	return suggestions

#TODO
def remove_duplicates(file_list):
	return

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
	#delete duplicates from directory
	remove_duplicates(gtr_135)

	#TODO
	#go through each file to rename
	if len(gtr_135)>0:
		print(str(len(gtr_135)) + ' files to rename:\n')
		for i in gtr_135:
			suggestions=suggest(i)
			#print(str(i) + '\n')
			

		
