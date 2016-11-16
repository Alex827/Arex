'''

File: everything.py
Author: Arex
Function: Does everything with functions
 
'''
#imports
import datetime

# 1x3 multidimensional array that stores [file size, date modified, file name]
#array for server files
global multiSerArr
#array for client files
global multiCliArr
multiSerArr = []
multiCliArr = []
#array for differences between the two
nameDiffArr = []

#checks for new files in server that are not in client
def checkForNewFiles():
	#max index for client files
	maxCliInd = 0
	#incremental var
	i = 0
	
	#if server has more files than client
	if len(multiSerArr) > len(multiCliArr):
		#for loop to go through files in client
		while i < len(multiCliArr):
			#if files is not found in client side
			if multiSerArr[maxCliInd][2] not in multiCliArr[i]:
				#add to difference array
				nameDiffArr.append(multiSerArr[maxCliInd][2])
				#decrement the incremental var so that the next file is correct
				i = i - 1
			#increment both indices
			maxCliInd += 1
			i += 1

		#adding in the rest of the server files to the difference array
		for j in range(maxCliInd, len(multiSerArr)):
			nameDiffArr.append(multiSerArr[j][2])
	
	#print out the files to be downloaded to be used in bash	
	if len(nameDiffArr) > 0:
		for i in range(0, len(nameDiffArr)):
			print(nameDiffArr[i])

#parses the client or server ls files and their info
#input: isServer = [0,1]
#	0 = parse client ls file
#	1 = parse server ls file
def parselsFiles(isServer):
	#header for which file to read
	header = ''
	#parse it with server indexes
	if isServer == 1:
		#multidimensional server file array
		global multiSerArr
		multiArr = multiSerArr
		header = 'server'
		#index to get file size
		fileSizeInd = 27
		#index to get file date
		dateInd = 36
		#index to get file name
		nameInd = 49
	#parse it with client indexes
	elif isServer == 0:
		#multidimensional client file array
		global multiCliArr
		multiArr = multiCliArr
		header = 'client'
		#index to get file size
		fileSizeInd = 32
		#index to get file date
		dateInd = 41
		#index to get file name
		nameInd = 54

	#file to parse
	toParse = '/tmp/' + header +'ls.txt'
	#an element that goes into the multidimentional array
	#this array should only have three elements
	#[file dize, file date, file name]
	tempFileArr = []
	
	#go through the ls files	
	with open(toParse) as file:
		#client ls file has total count as line one, so we skip it
		if isServer == 0:
			file.readline()
		#save the lines
		lines = file.readlines()
		#for every line
		for i in lines:
			#save the file size	
			fileSize = i[fileSizeInd:dateInd-1]
			tempFileArr.append(fileSize)
			#saves the file date
			date = i[dateInd:nameInd]
			#it gets converted into a date object using the method convertToDateObj()
			tempFileArr.append(convertToDateObj(date))
			#save file name	
			name = i[nameInd:]
			name = name.strip('\n')
			tempFileArr.append(name)
			#add the array into the multidimensional array	
			multiArr.append(tempFileArr)
			#reset array for next file
			tempFileArr = []

#parse both server and ls files altogether
def parseBoth():
	global multiSerArr
	global multiCliArr

	multiSerArr = []
	multiCliArr = []
	#parsing server files		
	parselsFiles(1)
	#parseing client files
	parselsFiles(0)

#converts input to a python datetime object
#input: toConvert = a string in the form of 'month, day, year'
#	months are in three letter alphabet form i.e. Jan, Feb, etc.
def convertToDateObj(toConvert):
	#indices for how to separate the string
	monthInd = 3
	dayInd = 6
	yearInd = 7

	#separate into the correct parts
	month = toConvert[:monthInd]
	day = toConvert[monthInd:dayInd]
	year = toConvert[yearInd:]
	#if it is the current year, it will give a time
	#so we convert the time to the current year instead
	if year.find(':') > 0:
		year = datetime.datetime.now().year
	#make a datetime object and return it
	#uses monthToNum to intergize the month
	fileDate = datetime.date(int(year), monthToNum(month), int(day))
	return fileDate 

#convert the three letter alphabet form of a month to the integer value
def monthToNum(month):
	if month == 'Jan':
		return 1
	if month == 'Feb':
		return 2
	if month == 'Mar':
		return 3
	if month == 'Apr':
		return 4
	if month == 'May':
		return 5
	if month == 'Jun':
		return 6
	if month == 'Jul':
		return 7
	if month == 'Aug':
		return 8
	if month == 'Sep':
		return 9
	if month == 'Oct':
		return 10
	if month == 'Nov':
		return 11
	if month == 'Dev':
		return 12

#find the problematic files
#problem = difference in size or date
def findProblematicFiles():
	print('\nChecking for problematic files\n')
	#array that will hold the problematic files
	probArr = []
	#the problems in strings
	sizeStr = 'File sizes are different'
	dateStr = 'File date is newer'
	bothStr = 'File sizes are different and date is newer'

	#reparse the server and client ls files after updating
	parseBoth()
	#go through all the server files
	for i in range(0, len(multiSerArr)):
		#go through the multidimensional array
		for j in range(0, 2):
			#j = 0 means the file size
			if j == 0:
				#if file size are different
				if multiSerArr[i][j] != multiCliArr[i][j]:
					probArr.append(multiSerArr[i][2] + ' ' + sizeStr)
			#j = 1 means the file date
			if j == 1:
				#if file date is newer
				if multiSerArr[i][j] > multiCliArr[i][j]:
					#go through the existing problem array
					for k in range(0, len(probArr)):
						#if element already exists, then updates ending string
						if probArr[k].find(multiSerArr[i][2]) > -1:
							probArr[k] = multiSerArr[i][2] + ' ' + bothStr
						#else add in date error string
						elif (k == len(probArr)-1) and (probArr[k].find(multiSerArr[i][2]) < 0):
							probArr.append(multiSerArr[i][2] + ' ' + dateStr)
	#go through the problem array and print out the elements and whats wrong with them	
	if len(probArr) > 0:
		print('The following files need to be manually checked for redownload: \n')
		for i in range(0, len(probArr)):
			print(probArr[i])
	#if no problems
	else:
		print('No problematic files\n')
	
		
#testing purposes, currently not needed
'''
def main():
	#space in front of name element
	parseBoth()
	for i in range(0, len(multiSerArr)):
		print("Server Array Names:",multiSerArr[i][2])
		print("Client Array Names:",multiCliArr[i][2])	
	checkForNewFiles()
	findProblematicFiles()
	print('Done')
'''
