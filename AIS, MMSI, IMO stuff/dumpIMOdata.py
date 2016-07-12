import sys
import urllib

def lineCheck(inputLine, inputStr):
	leng = len(inputStr)
	if inputLine[inputLine.find(inputStr)+leng] is not ' ':
		return inputLine[inputLine.find(inputStr):]
	else:
		return ''
		
def exnameCheck(inputStr):
	if exname1 is not '':
		inputStr = inputStr + exname1
	if exname2 is not '':
		inputStr = inputStr + exname1
	if exname3 is not '':
		inputStr = inputStr + exname1
	if exname4 is not '':
		inputStr = inputStr + exname1
	if exname5 is not '':
		inputStr = inputStr + exname1
	if exname6 is not '':
		inputStr = inputStr + exname1
	if exname7 is not '':
		inputStr = inputStr + exname1
	if exname8 is not '':
		inputStr = inputStr + exname1
	if exname9 is not '':
		inputStr = inputStr + exname1
	return inputStr

numIMO = sys.argv[1]
link = "http://www.containership-info.com/vessel_" + numIMO + (".html")
file = numIMO + ".html"
urllib.urlretrieve(link,file)

with open(file) as f:
	for line in f:
		if line.find("1st name: ") > -1:
			firstName = lineCheck(line, "1st name: ")
		if line.find("/ nationality: ") > -1:
			flagNat = lineCheck(line, "/ nationality: ")
			stripInt = flagNat.find("<")
			flagNat = flagNat[:stripInt]
		if line.find("owner: ") > -1:
			owner = lineCheck(line, "owner: ")
		if line.find("operator: ") > -1:
			operator = lineCheck(line, "operatore: ")
		if line.find("completion year: ") > -1:
			completionYear = lineCheck(line, "completion year: ")
		if line.find("shipyard: ") > -1:
			shipYard = lineCheck(line, "shipyard: ")
		if line.find("yard / hull number: ") > -1:
			yard = lineCheck(line, "yard / hull number: ")
		if line.find("engine design: ") > -1:
			engineDes = lineCheck(line, "engine design: ")
		if line.find("engine type: ") > -1:
			engineType = lineCheck(line, "engine type: ")
		if line.find("power output (KW): ") > -1:
			power = lineCheck(line, "power output (KW): ")
		if line.find("maximum speed (Kn): ") > -1:
			maxSpd = lineCheck(line, "maximum speed (Kn): ")
		if line.find("overall length (m): ") > -1:
			overallLen = lineCheck(line, "overall length (m): ")
		if line.find("overall beam (m): ") > -1:
			overallBeam = lineCheck(line, "overall beam (m): ")
		if line.find("maximum draught (m): ") > -1:
			maxDraught = lineCheck(line, "maximum draught (m): ")
		if line.find("maximum TEU capacity: ") > -1:
			maxTEU = lineCheck(line, "maximum TEU capacity: ")
		if line.find("container capacity at 14t (TEU): ") > -1:
			contCapacity = lineCheck(line, "container capacity at 14t (TEU): ")
		if line.find("reefer containers (TEU): ") > -1:
			reeferCont = lineCheck(line, "reefer containers (TEU): ")
		if line.find("deadweight (ton): ") > -1:
			deadweight = lineCheck(line, "deadweight (ton): ")
		if line.find("gross tonnage (ton): ") > -1:
			grossTon = lineCheck(line, "gross tonnage (ton): ")
		if line.find("handling gear: ") > -1:
			handGear = lineCheck(line, "handling gear: ")
		if line.find("exname 1: ") > -1:
			exname1 = lineCheck(line, "exname 1: ")
		if line.find("exname 2: ") > -1:
			exname2 = lineCheck(line, "exname 2: ")
		if line.find("exname 3: ") > -1:
			exname3 = lineCheck(line, "exname 3: ")
		if line.find("exname 4: ") > -1:
			exname4 = lineCheck(line, "exname 4: ")
		if line.find("exname 5: ") > -1:
			exname5 = lineCheck(line, "exname 5: ")
		if line.find("exname 6: ") > -1:
			exname6 = lineCheck(line, "exname 6: ")
		if line.find("exname 7: ") > -1:
			exname7 = lineCheck(line, "exname 7: ")
		if line.find("exname 8: ") > -1:
			exname8 = lineCheck(line, "exname 8: ")
		if line.find("exname 9: ") > -1:
			exname9 = lineCheck(line, "exname 9: ")

outputString = ("\n" + firstName + "\n"
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
+ maxSpd + "\n"
+ overallLen + "\n"
+ overallBeam + "\n"
+ maxDraught + "\n"
+ maxTEU + "\n"
+ contCapacity + "\n"
+ reeferCont + "\n"
+ deadweight + "\n"
+ grossTon + "\n"
+ handGear.strip("\n") + "\n")

outputString = exnameCheck(outputString)

print(outputString)
