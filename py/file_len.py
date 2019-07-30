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

	#search for and remove '(COMIC....)' text
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

	#if the first character in the file name is '[' then i remove
	#the first element of square_brackets from the list because 
	#that particular instance is the author
	#take author out of temp and use it for later
	author=''
	if temp[0] == '[':
		author=square_brackets.pop(0)
		temp=temp.replace(author, '').strip()

	for i in square_brackets:
		temp=temp.replace(i, '').strip()

	#see if there's a substring with parentheses at the end and exctract it
	#usually it contains the original series info but sometimes it's useless bs
	#2 different operations: append to the different strings if temp gets split from the '   ' substring
	#or i add the string without the parentheses substring to the suggestions list
	############ doesn't work if there's a duplicate which has '(1)' added to the end of it
	############ remove_duplicates function will take care of that
	parentheses=re.findall('\(.*?\)', temp)
	paren_substr=None
	if temp[-1] == ')':
		paren_substr=parentheses[-1]
		temp=temp.replace(paren_substr, '').strip()

	#find and replace the substring '   ' and store the new string
	#if the new string is less than 135 characters then return a  
	#list with just the new string
	#TODO
	space_index=temp.find('   ')
	temp_nomultspace=temp  #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< remember this
	if space_index > -1:
		temp_nomultspace=temp.replace('   ', ' ')
		
	if len(author) + len(temp_nomultspace) + len(parentheses) + 2 > 135:# +2 because of the spaces
		print('------------------------------')
		print('space index:\t\t' + str(space_index))
		print('original:\t\t' + author + ' ' +  temp)
		if(space_index>-1):
			print('space trimmed:\t\t' + author + ' ' +  temp_nomultspace)
			if(paren_substr is not None):
				print('1st substr:\t\t' + author + ' ' +  temp_nomultspace[:space_index] + ' ' + paren_substr)
				print('2nd substr:\t\t' + author + ' ' +  temp_nomultspace[space_index+1:] + ' ' + paren_substr)
			else:
				print('1st substr:\t\t' + author + ' ' +  temp_nomultspace[:space_index])
				print('2nd substr:\t\t' + author + ' ' +  temp_nomultspace[space_index+1:])
		print('------------------------------')
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
			

		
