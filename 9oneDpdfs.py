import scipy.stats
from matplotlib import pyplot as plt,cm as mpl_cm,lines as mpl_lines,colorbar

def m1m2fromMcq(Mc,q):

	m1 = Mc*((1+q)/q**3)**0.2
	m2 = Mc*(q**2 * (1+q))**0.2
	if m1<m2:
		m1,m2 = m2,m1

	return m1, m2

file = open('posterior_samples.dat')
filedata = file.readlines()
file.close()

postSamp = [[] for i in range(9)]
num = [11, 10, 8, 6,5,7,3,4,9]
names = ["$\mathcal{M}_c$","$q$","$\phi_c$","$\\alpha$","$\delta$","$D$","$\iota$","$\psi$","$Time$"]
xaxis = ["Chirp Mass $(M_{\odot})$","Mass Ratio","Chirp Phase $(rad.)$","Right Ascension $(rad.)$","Declination $(rad.)$","Distance $(MPC)$","Inclination $(rad.)$","Polarization $(rad.)$","Time $(msec.)$"]
inject = [1.21877,.999,2.68833,4.662361,-0.4254096,99.15952,2.353028,2.153679,0.]
ticks = [[1.2183,1.2185,1.2187,1.2189],
         [0.7,0.75,0.8,0.85,0.9,0.95,1],
		 [0,1,2,3,4,5,6],
		 [4.65,4.66,4.67,4.68,4.69],
		 [-0.6,-0.55,-0.5,-0.45,-0.4,-0.35],
		 [40,60,80,100,120,140,160,180],
		 [1.8,2,2.2,2.4,2.6,2.8,3.0],
		 [0,0.5,1,1.5,2,2.5,3,3.5],
		 [-2,-1,0,1]]
		 

for i in range(1,len(filedata)):
	for j in range(9):
			postSamp[j].append(float(filedata[i].split()[num[j]]))
	#		if j==1:
	#			m1, m2 = m1m2fromMcq(postSamp[0][i-1],postSamp[1][i-1])
	#			postSamp[1][i-1] = m1*m2 / (m1+m2)**2 
			if j == 8:
				postSamp[j][i-1] = (postSamp[j][i-1] - 894429279.)*1000

for j in range(9):
	postSamp[j].sort()

#this part reflects the data across boundares for the purposes of the KDE.
#for q, it reflects across the q=1 boundary, while it wraps data around for the 
# phi_0 and psi boundaries
for i in range(1,1200):  
	postSamp[1].append(2-postSamp[1][-2*i + 1])  
for i in range(1,2000):  
	postSamp[2].insert(0, -(2*pi - postSamp[2][-2*i + 1]))
	postSamp[2].append(2*pi + postSamp[2][2*i - 1 ]) 
	postSamp[7].insert(0, -(pi - postSamp[7][-2*i + 1]))
	postSamp[7].append(pi + postSamp[7][2*i - 1 ])

KDEdataX = []
KDEdataY = []

suptitle("Example 1D Posterior Probability Densities for $1.4M_{\odot}/1.4M_{\odot}$ System", fontsize=26)
for i in range(9):
		KDE = scipy.stats.gaussian_kde(postSamp[i])
		#KDE.set_bandwidth(bw_method=KDE.factor / 2.)
		m1Min = min(postSamp[i])
		m1Max = max(postSamp[i])
		if i == 1:
			m1Max = 1
		if i == 2:
			m1Max = 2*pi
			m1Min = 0
		if i == 7:
			m1Max = pi
			m1Min = 0
		dx = (m1Max- m1Min) / 1000.
		n = m1Min
		while n <= m1Max:
			KDEdataX.append(n)
			KDEdataY.append(float(KDE(n)))
			n += dx
		ax1 = subplot(3,3,i+1)
		#hist(postSamp[i],40)
		ax1.plot(KDEdataX,KDEdataY,lw=1,color='black')
		ax1.fill_between(KDEdataX,KDEdataY,zeros(len(KDEdataY)), alpha=0.7, color="blue")
		xlabel(xaxis[i])
		ylabel("Posterior Probability")
		#ax1.hist(postSamp[i],bins=30,alpha=0.7)
		ax1.grid("on")
		ax1.set_xticks(ticks[i])
		axvline(inject[i],color='red', lw=3,linestyle="--")
		title(names[i], fontsize = 22)
		KDEdataX = []
		KDEdataY = []

show()
