import os
from os import listdir
from os.path import isfile, join
import re

#constants
MAX_FILE_LEN=135



'''
suggest file names for a given string
'''
def suggest(fname):

	file_ext=fname[fname.rfind('.'):]
	fname_no_ext=fname[:fname.rfind('.')]

	#use temp instead of fname to avoid confusion
	suggestions=[]
	temp=fname_no_ext

	#remove substrings enclosed by parentheses at the beginning of the string
	if temp[0] == '(':
		prefix_brackets=re.findall('\(.*?\)', temp)
		temp=temp.replace(prefix_brackets[0], '').strip()
		print(prefix_brackets[0])

	#remove substrings beginning and ending with curly brackets
	curly_brackets=re.findall('\{.*?\}', temp)
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
	paren_substr=''
	if temp[-1] == ')':
		temp=temp.replace(parentheses[-1], '').strip()
		paren_substr=' ' + parentheses[-1] # prepend ' ' so i don't have to add it in later

	#find and replace the substring '   ' and store the new string
	#if the new string is less than 135 characters then return a  
	#list with just the new string
	#TODO
	space_index=temp.find('   ')

	if space_index > -1:
		temp=temp.replace('   ', ' ')

	#create suggestions list to return
	if len((author + ' ' + temp + paren_substr + file_ext)) < MAX_FILE_LEN:
		return [(author + ' ' + temp + paren_substr + file_ext)]
	else:
		if(space_index>-1):
			suggestions.append(author + ' ' + temp[:space_index] + paren_substr + file_ext)
			suggestions.append(author + ' ' + temp[space_index+1:] + paren_substr + file_ext)
			return suggestions
		else:
			return []

'''
removes all duplicate files from the directory. not just files with names > 135 characters
'''
def remove_all_duplicates(file_list, cwd):
	print('REMOVING DUPLICATES')
	for i in file_list:
		no_duplicates=[]
		file_ext=i[i.rfind('.'):]
		fname_no_ext=i[:i.rfind('.')]
		#see if the file name w/o the extension has a (#) substring
		#seeing that at the end in my case means it's a file duplicate
		if fname_no_ext[-1] == ')':
			parentheses = re.findall('\([0-9]*?\)', fname_no_ext)
			
			#checks if file with the same name minus the '(#)' string at the end exists in file_list
			if (fname_no_ext.replace(parentheses[-1], '').strip() + file_ext) in file_list:
				os.remove(cwd + '/' + i)
				print('deleted ' + i)
		else:
			no_duplicates.append(i)

	print('DUPLICATES REMOVED\n\n')
	return no_duplicates

if __name__ == '__main__':
	#get current working directory
	cwd=os.getcwd()
	gtr_max_len=[]
	smallest_gtr_35=''
	test_list=[]


	#delete all duplicates from directory
	#gtr_max_len=remove_duplicates(gtr_max_len)
	all_files=listdir(cwd)
	all_files=remove_all_duplicates(all_files, cwd)

	#create list of files that exceed MAX_FILE_LEN
	for f in all_files:
		potential_file=f

		if len(f) > MAX_FILE_LEN:
			gtr_max_len.append(f)

			if smallest_gtr_35=='' or len(f)<len(smallest_gtr_35):
				smallest_gtr_35=f
			
	
	#TODO
	#go through each file to rename
	#create a list of suggestions and prompt for which file name to take
	if len(gtr_max_len)>0:
		print(str(len(gtr_max_len)) + ' files to rename:\n')
		for i in gtr_max_len:
			suggestions=suggest(i)
			print('-----------------------------------------------------')
			if len(suggestions) != 0:
				print('Suggestions for \'' + i + '\'\n')
				for j in range(len(suggestions)):
					print('(' + j + '): ' + suggestions[j])

				choice = input('Enter number for new file name: ')
				print('you entered: ' + choice)
			else:
				print('Unable to automatically reduce file name')
				new_name = input('Manually enter new name: \n')
				print(new_name)
			print('-----------------------------------------------------')
			print('\n')

		
