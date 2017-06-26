'''

File: diffLSfiles.py
Author: Arex
Function: Finds the difference in filenames between the client and
	the server
 
'''


#getting the ls files
filesOnServer = '/home/aisadmin/scripts/AISFTP/strippedLS.txt'
filesOnClient = '/home/aisadmin/scripts/AISFTP/clientFiles.txt'

#putting the file names into arrays
arrOfCliF = []
arrOfSerF = []
diffArrToRet = []

#putting client filenames into an array
with open(filesOnClient) as clientF:
	arrOfCliF = clientF.readlines()

#comparing files
with open(filesOnServer) as serverF:
	#putting server filesnames into an array
	arrOfSerF = serverF.readlines()
	#if client has less files than server
	if len(arrOfCliF) < len(arrOfSerF):
		#if server has files not in client, then add to diff array
		for i in range(0, len(arrOfSerF)):
			if arrOfSerF[i] not in arrOfCliF:
				diffArrToRet.append(arrOfSerF[i]);

#		toCont = 0
#		#if files are different, then add to difference array
#		for i in range(0, len(arrOfSerF)):
#			if toCont == 1:
#				toCont = 0
#				continue;
#			for j in range(0, len(arrOfCliF)):
#				if arrOfCliF[j].find("filesList") > 0:
#					continue;
#				if arrOfSerF[i] != arrOfCliF[j]:
#					diffArrToRet.append(arrOfSerF[i])
#					toCont = 1

#prints the files to stdout for bash to take in as variable
for i in range(0, len(diffArrToRet)):
	print(diffArrToRet[i])
