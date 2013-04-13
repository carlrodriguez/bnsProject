#!/opt/local/bin/python
from math import *

file = open('ranked_sky_pixels.dat')
filedata = file.readlines()
file.close()

i = 0
cum = float(filedata[1].split()[3]) 
maxLra= float(filedata[1].split()[1])*0.26179938779
maxLdec = float(filedata[1].split()[0])*0.01745329251

while cum <= 0.6827: #one sigma
	cum = float(filedata[i+2].split()[3]) 
	i += 1


radOut = i*(12.56637) / (len(filedata) - 1)
degOut = i*(41252.96129655765) / (len(filedata) - 1)

dPhi = sqrt(radOut/6.28318530718)

dSigmaCircle = acos(sin(maxLdec)**2 + (cos(maxLdec)**2)*cos(dPhi))

j = 1
numInCircle = 1.
cum = 0
while cum <= 0.6827: #one sigma
	cum = float(filedata[j+1].split()[3]) 
	ra= float(filedata[j+1].split()[1])*0.26179938779
	dec = float(filedata[j+1].split()[0])*0.01745329251
	dSigma= acos(sin(maxLdec)*sin(dec) + cos(maxLdec)*cos(dec)*cos(maxLra - ra))
	if dSigma < dSigmaCircle:
		numInCircle += 1.
	j += 1

print maxLra, maxLdec, degOut, (numInCircle/i)*100 
