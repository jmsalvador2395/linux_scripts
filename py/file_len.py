import os
from os import listdir
from os.path import isfile, join


if __name__ == '__main__':
	cwd=os.getcwd()
	#onlyfiles=[]
	gtr_45=[]
	lsseq_45=[]
	for f in listdir(cwd):
		#potential_file=join(cwd, f)
		potential_file=f
		if len(f) > 45:
			gtr_45.append(f)
		else:
			lsseq_45.append(f)
		'''
		if isfile(potential_file):
			onlyfiles.append(potential_file)
		'''
	print 'greater than 45:'
	for i in gtr_45:
		print i
	
	print '45 and less:'
	for i in lsseq_45:
		print i
			
			
