#toRead = input('File to read: ')
#toWrite = input('File to write to: ')
toRead = r"D:\old.xml" 
toWrite = r"D:\new.xml"

arrOfKeys = []
arrOfTags = []

testArr = []
#i = 0

with open(toRead) as f1:
	for line1 in f1:
		#getting the tag names
		index0 = line1.find('Computer')
		index1 = line1.find('">')
		if index0 > 0:
			tagsToFind = line1[index0 : index1+1]
			arrOfTags.append(tagsToFind)	
			#i += 1
			
		#getting the keys corresponding to tag names
		if index0 > 0:
			keysToFind = line1[index1 + 2:index1 + 30]
			arrOfKeys.append(keysToFind)


a = open(r"D:\test.xml","w")
			
with open(toWrite, "r+") as f2:
	for line2 in f2:
		i = 0
		#finding correct keys
		if (line2.find('8/1/2011') > 0):
			indexEnd = line2.find('">')
			for keys in arrOfKeys:
				if (line2.find(keys) > 0):
					line2 = line2[:indexEnd + 1] + ' ' + arrOfTags[i][:-1] + line2[indexEnd:]
				i += 1
		a.write(line2)

	
'''
for keys in arrOfKeys:
	print(keys)
'''
#print(i)
'''
for tags in arrOfTags:
	print(tags)
'''		

