#importing packages
import sys
import urllib
import os

#Helper Methods
#gets the correct text from HTML (strips HTML stuff)
def lineCheck(inputLine, inputStr, title):
	#index pointer
	leng = len(inputStr)
	#if field is not empty
	if inputLine[inputLine.find(inputStr)+leng] is not ' ':
		#to get title
		if title == True:
			return inputLine[inputLine.find(inputStr)+leng:].replace("</TITLE>", "")
		#strip html
		else:
			return inputLine[inputLine.find(inputStr):]
	#else return nothing
	else:
		return ''

#checks for all exnames
def exnameCheck(inputStr):
	#if there is an exname, then put it into final string
	if exname1 is not '':
		inputStr = inputStr + exname1 + "\n"
	if exname2 is not '':
		inputStr = inputStr + exname2 + "\n"
	if exname3 is not '':
		inputStr = inputStr + exname3 + "\n"
	if exname4 is not '':
		inputStr = inputStr + exname4 + "\n"
	if exname5 is not '':
		inputStr = inputStr + exname5 + "\n"
	if exname6 is not '':
		inputStr = inputStr + exname6 + "\n"
	if exname7 is not '':
		inputStr = inputStr + exname7 + "\n"
	if exname8 is not '':
		inputStr = inputStr + exname8 + "\n"
	if exname9 is not '':
		inputStr = inputStr + exname9 + "\n"
	return inputStr

#IMO input number
numIMO = sys.argv[1]
#link to database
link = "http://www.containership-info.com/vessel_" + numIMO + (".html")
#makes a new file
file = numIMO + ".html"
#downloads the file
urllib.urlretrieve(link,file)

with open(file) as f:
	for line in f:
		#if no such IMO in database
		if line.find("404") > -1:
			print("\nIMO number not found in database")
			os.remove(file)
			sys.exit()
		#gets all necessary info
		if line.find("<TITLE>"+str(numIMO)+"_") > -1:
			title = lineCheck(line, "<TITLE>"+str(numIMO+"_"), True)
		if line.find("1st name: ") > -1:
			firstName = lineCheck(line, "1st name: ", False)
		if line.find("/ nationality: ") > -1:
			flagNat = lineCheck(line, "/ nationality: ", False)
			stripInt = flagNat.find("<")
			flagNat = flagNat[:stripInt]
		if line.find("owner: ") > -1:
			owner = lineCheck(line, "owner: ", False)
		if line.find("operator: ") > -1:
			operator = lineCheck(line, "operatore: ", False)
		if line.find("completion year: ") > -1:
			completionYear = lineCheck(line, "completion year: ", False)
		if line.find("shipyard: ") > -1:
			shipYard = lineCheck(line, "shipyard: ", False)
		if line.find("yard / hull number: ") > -1:
			yard = lineCheck(line, "yard / hull number: ", False)
		if line.find("engine design: ") > -1:
			engineDes = lineCheck(line, "engine design: ", False)
		if line.find("engine type: ") > -1:
			engineType = lineCheck(line, "engine type: ", False)
		if line.find("power output (KW): ") > -1:
			power = lineCheck(line, "power output (KW): ", False)
		if line.find("maximum speed (Kn): ") > -1:
			maxSpd = lineCheck(line, "maximum speed (Kn): ", False)
		if line.find("overall length (m): ") > -1:
			overallLen = lineCheck(line, "overall length (m): ", False)
		if line.find("overall beam (m): ") > -1:
			overallBeam = lineCheck(line, "overall beam (m): ", False)
		if line.find("maximum draught (m): ") > -1:
			maxDraught = lineCheck(line, "maximum draught (m): ", False)
		if line.find("maximum TEU capacity: ") > -1:
			maxTEU = lineCheck(line, "maximum TEU capacity: ", False)
		if line.find("container capacity at 14t (TEU): ") > -1:
			contCapacity = lineCheck(line, "container capacity at 14t (TEU): ", False)
		if line.find("reefer containers (TEU): ") > -1:
			reeferCont = lineCheck(line, "reefer containers (TEU): ", False)
		if line.find("deadweight (ton): ") > -1:
			deadweight = lineCheck(line, "deadweight (ton): ", False)
		if line.find("gross tonnage (ton): ") > -1:
			grossTon = lineCheck(line, "gross tonnage (ton): ", False)
		if line.find("handling gear: ") > -1:
			handGear = lineCheck(line, "handling gear: ", False)
		if line.find("exname 1: ") > -1:
			exname1 = lineCheck(line, "exname 1: ", False)
		if line.find("exname 2: ") > -1:
			exname2 = lineCheck(line, "exname 2: ", False)
		if line.find("exname 3: ") > -1:
			exname3 = lineCheck(line, "exname 3: ", False)
		if line.find("exname 4: ") > -1:
			exname4 = lineCheck(line, "exname 4: ", False)
		if line.find("exname 5: ") > -1:
			exname5 = lineCheck(line, "exname 5: ", False)
		if line.find("exname 6: ") > -1:
			exname6 = lineCheck(line, "exname 6: ", False)
		if line.find("exname 7: ") > -1:
			exname7 = lineCheck(line, "exname 7: ", False)
		if line.find("exname 8: ") > -1:
			exname8 = lineCheck(line, "exname 8: ", False)
		if line.find("exname 9: ") > -1:
			exname9 = lineCheck(line, "exname 9: ", False)

#put all info into final string
outputString = ("\nTitle: " + title + "\n"
+ firstName + "\n"
+ "IMO number: " + numIMO + "\n\n"
+ "flag " + flagNat + "\n\n"
+ owner.strip("\n")
+ operator + "\n"
+ completionYear + "\n"
+ shipYard + "\n"
+ yard + "\n"
+ engineDes + "\n"
+ engineType + "\n"
+ power + "\n"
+ maxSpd.replace(",","") + "\n"
+ overallLen.replace(",","") + "\n"
+ overallBeam.replace(",","") + "\n"
+ maxDraught.replace(",","") + "\n"
+ maxTEU.strip("\n") + "\n"
+ contCapacity + "\n"
+ reeferCont + "\n"
+ deadweight + "\n"
+ grossTon + "\n"
+ handGear + "\n")

#put in exnames if any
outputString = exnameCheck(outputString)

#print final string
print(outputString)

#remove the file
os.remove(file)
