#!/usr/bin/env python
import sys

intCodeStr = sys.stdin.readline()
intCodesList = intCodeStr.split(",")
intCodesList[-1] = intCodesList[-1].strip("\n")
intCodesFresh = []
for string in intCodesList:
	intCodesFresh.append(int(string))
for noun in range(99):
	for verb in range (99):
		intCodes = intCodesFresh[:]
		intCodes[1] = noun
		intCodes[2] = verb
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
		if intCodes[0]==19690720:
			print "Solution2b: " + str(100 * noun + verb)
			sys.exit()




