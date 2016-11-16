import shutil

#shutil.move('/home/aisadmin/AISdata_logfiles/SBARC/serverls.txt','/tmp/')

newFile = open('/tmp/test_names_only.txt','w')


toParse = '/tmp/test.txt'

fileSizeInd = 27
dateInd = 36
nameInd = 48

multiArr = []
tempFileArr = []

with open(toParse) as file:
	lines = file.readlines()
	for i in lines:
		fileSize = i[fileSizeInd:dateInd-1]
		tempFileArr.append(fileSize)

		date = i[dateInd:nameInd]
		tempFileArr.append(date)

		name = i[nameInd+1:]
		newFile.write(name)
		name = name.strip('\n')
		tempFileArr.append(name)

		multiArr.append(tempFileArr)
		tempFileArr = []
'''
for i in range(0, len(multiArr)):
	print(multiArr[i])		
'''

