'''

File: splitLSfiles.py
Author: Arex
Function: Formats the ls contents from the server to have
	only the filenames. Basically, strips all the extra
	ls data and keep only the filenames.

'''

import os
import shutil

#the file to strip to just names
toStrip = '/home/aisadmin/AISdata_logfiles/SBARC/serverls.txt'

#the new file to add the stripped names to
newFile = open('/tmp/serverls_names_only.txt', 'w')

#loop through all the lines to get only the names
with open(toStrip) as file:
	#read every line
	lines = file.readlines()
	#only get the filenames from every line
	for i in lines:
		toSplitIndex = i.find('AIS_')
		i = i[toSplitIndex:]
		newFile.write(i)

#move the original ls file to tmp folder
shutil.copy(toStrip, '/tmp/')


#remove the original ls file that is not needed	
os.remove(toStrip)	
