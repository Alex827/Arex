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
		#keeps track of max number of files in client list as an index
		maxInd = 0;
		#if files are different, then add to difference array
		for i in range(0, len(arrOfCliF)):
			#print(arrOfCliF[i])
			if arrOfCliF[i] != arrOfSerF[i]:
				diffArrToRet.append(arrOfSerF[i])
			maxInd = i
		#add remaining files from server list to difference array
		for j in range(maxInd, len(arrOfSerF)):
			diffArrToRet.append(arrOfSerF[j])

#prints the files to stdout for bash to take in as variable
for i in range(0, len(diffArrToRet)):
	print(diffArrToRet[i])
