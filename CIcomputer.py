#!/software/enthought/python/epd_free-7.3.2-rh6-x86_64/bin/python
import os.path
import numpy as np

def m1m2fromMcq(Mc,q):

    m1 = Mc*((1+q)/q**3)**0.2
    m2 = Mc*(q**2 * (1+q))**0.2
    if m1<m2:
        m1,m2 = m2,m1

    return m1, m2

def ciInterval(samples, ciInt):
	percent = (100. - ciInt) / 2.
	numSamplesToRemove = int(round(len(samples)*percent/100.))
	sortedSamples = sorted(samples)
	lower = sortedSamples[numSamplesToRemove]
	upper = sortedSamples[-numSamplesToRemove]
	return (upper , lower)

injectM1 = [1.,1.4,2.5,2.5]
injectM2 = [1.,1.4,1.,2.5]
injectQ = [1.,1.,0.4,1.]
injectMC = [0.8705506,1.218771,1.348809,2.176376]
params = ['mc','m1','m2','mtot','q','dist','iota','ra','dec','sa']
masses = ['1_1/','1.4_1.4/','1_2.5/','2.5_2.5/']

l = 0

for mass in masses:
	posteriorSamples = [[[]for i in range(40)]for k in range(10)]

	for i in range(40):
		filename = mass + str(i) + '/posterior_samples.dat'
		if os.path.exists(filename):
			file = open(filename)
			filedata = file.readlines()
			for j in range(1,len(filedata)):
				[cycle,logpost,logprior,iota,psi,dec,ra,dist,phi_orb,time,q,mc,logl,loglh1,logll1,loglv1,logli1,f_lower,chain] = filedata[j].split()
				posteriorSamples[0][i].append(float(mc)/injectMC[l])
				m1, m2 = m1m2fromMcq(float(mc),float(q))
				posteriorSamples[1][i].append(float(m1)/injectM1[l])
				posteriorSamples[2][i].append(float(m2)/injectM2[l])
				posteriorSamples[3][i].append((float(m1) + float(m2))/(injectM1[l] + injectM2[l]))
				posteriorSamples[4][i].append(float(q))
				posteriorSamples[5][i].append(float(dist))
				posteriorSamples[6][i].append(abs(np.cos(float(iota))))
				posteriorSamples[7][i].append(float(ra)*180/np.pi)
				posteriorSamples[8][i].append(float(dec)*180/np.pi)
			file.close()
		skyPixels = mass + str(i) + '/post/ranked_sky_pixels.dat'
		if os.path.exists(skyPixels):
			pixel = 0
			file = open(skyPixels)
			pixelData = file.readlines()
			file.close()
			cum = float(pixelData[1].split()[3])
			while cum <= 0.65:
				pixel += 1
				cum = float(pixelData[pixel+1].split()[3])
			posteriorSamples[9][i].append(pixel*(41252.96129655765) / (len(pixelData) - 1))

	l += 1
	intervals = [[]for i in range(10)]
	lowers = [[]for i in range(10)]
	uppers = [[]for i in range(10)]
	print 'mass Bin: ' + mass
	for i in range(9):
		for j in range(40):
			if posteriorSamples[i][j] != []:
				interval = ciInterval(posteriorSamples[i][j],65)
				intervals[i].append(interval[0] - interval[1])
				lowers[i].append(interval[1])
				uppers[i].append(interval[0])
		print params[i] + ': mean:' + str(np.mean(intervals[i])) + ': lower:' + str(np.mean(lowers[i])) + ': upper:' + str(np.mean(uppers[i]))

	for i in range(40):
		intervals[9].append(posteriorSamples[9][i])
	print params[9] + ': mean:' + str(np.mean(intervals[9])) + ': max:' + str(max(intervals[9])) + ': min:' + str(min(intervals[9])) 
	string = ''
	for i in range(5,10):
		string += "$%.2e}$" % (np.mean(intervals[i])) +  " & \\vlin & " 
	string = string.replace('e','\\times 10^{')
	string = string.replace('vlin','vline')
	string = string.replace('+0','')
	string = string.replace('-0','-')
	string = string.replace('\\times 10^{0}','')
	print string.rstrip(' & \\vline & ') + '\\\\'
	

	print '\n'
