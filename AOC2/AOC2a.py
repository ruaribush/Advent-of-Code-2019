#!/usr/bin/env python
import sys

intCodeStr = sys.stdin.readline()
intCodesList = intCodeStr.split(",")
intCodesList[-1] = intCodesList[-1].strip("\n")
intCodes = []
for string in intCodesList:
	intCodes.append(int(string))
intCodes[1] = 12
intCodes[2] = 2
counter = 0
while counter < len(intCodes):
	if intCodes[counter] == 99:
		break;
	else:
		inputloc1 = intCodes[counter+1]
		inputloc2 = intCodes[counter+2]
		storeloc = intCodes[counter+3]
		if intCodes[counter] == 1:
			#adding
			intCodes[storeloc] = intCodes[inputloc1]+intCodes[inputloc2]
			counter +=3
		elif intCodes[counter] == 2:
			#multiplying
			intCodes[storeloc] = intCodes[inputloc1]*intCodes[inputloc2]
			counter +=3
		else:
			print "Oh deary me"
	counter += 1
print "Solution2a: " + str(intCodes[0])




