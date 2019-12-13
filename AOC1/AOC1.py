#!/usr/bin/env python
import sys

def sumFuel(moduleList):
	total=0
	for module in moduleList:
		total+=getFuel(module)
	return total

def sumFuelAvd(moduleList):
	total=0
	for module in moduleList:
		total+=getAdditionalFuelMass(module)
	return total

def getFuel(mass):
	return (mass/3)-2

def getAdditionalFuelMass(mass):
	fuelMass = getFuel(mass)
	if fuelMass>0:
		return fuelMass+getAdditionalFuelMass(fuelMass)
	return 0

masses = []
for mass in sys.stdin:
	masses.append(int(mass))

print "Solution 1a:"+str(sumFuel(masses))
print "Solution 1b:"+str(sumFuelAvd(masses))







