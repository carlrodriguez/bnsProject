import scipy.stats
from matplotlib import pyplot as plt,cm as mpl_cm,lines as mpl_lines,colorbar

def m1m2fromMcq(Mc,q):

	m1 = Mc*((1+q)/q**3)**0.2
	m2 = Mc*(q**2 * (1+q))**0.2
	if m1<m2:
		m1,m2 = m2,m1

	return m1, m2

massBins = ['11','1414','125','2525']
chirpMasses = [0.8705506, 1.218771, 1.348809, 2.176376]
massRatios = [1,1,0.4,1]
indivMasses = [(1.,1.),(1.4,1.4),(1.,2.5),(2.5,2.5)]
Bin = 0
colors=['black','blue','red','green']

for number in massBins:
		file = open('mc' + number + 'Meta.dat')
		mcdata = file.readlines()
		file.close()
		file = open('q' + number +'Meta.dat')
		qdata = file.readlines()
		file.close()

		q  = []
		mc = []
		m1 = []
		m2 = []
		M  = []
		k = 0

		for i in range(0,len(mcdata),20):
			q.append(float(qdata[i].rstrip()))
			mc.append(float(mcdata[i].rstrip())/chirpMasses[Bin])
			m1Temp, m2Temp = m1m2fromMcq(mc[k]*chirpMasses[Bin],q[k])
			m1.append(m1Temp / indivMasses[Bin][1])
			m2.append(m2Temp / indivMasses[Bin][0])
			M.append((m1Temp + m2Temp)/sum(indivMasses[Bin]))
			k += 1
		print min(M)

		m1KDE = scipy.stats.gaussian_kde(m1)
		m2KDE = scipy.stats.gaussian_kde(m2)
		mcKDE = scipy.stats.gaussian_kde(mc)
		mKDE  = scipy.stats.gaussian_kde(M)
		qKDE  = scipy.stats.gaussian_kde(q)

		Xm1 = []
		Ym1 = []
		Xm2 = []
		Ym2 = []
		Xmc = []
		Ymc = []
		Xm  = []
		Ym  = []
		Xq  = []
		Yq  = []

		m1Min = min(m1)
		m1Max = max(m1)
		dx = (m1Max- m1Min) / 1000.
		n = m1Min

		while n <= m1Max:
			Xm1.append(n)
			Ym1.append(float(m1KDE(n)))
			n += dx

		m2Min = min(m2)
		m2Max = max(m2)
		dx = (m2Max - m2Min) / 1000.
		n = m2Min

		while n <= m2Max:
			Xm2.append(n)
			Ym2.append(float(m2KDE(n)))
			n += dx

		ax1 = subplot(3,1,1)
		fill_between(Xm1,Ym1,zeros(len(Ym1)), alpha=0.3, color=colors[Bin])
		plot(Xm1,Ym1, color=colors[Bin], linestyle='solid', lw=3)
		fill_between(Xm2,Ym2,zeros(len(Ym2)), alpha=0.4, color=colors[Bin])
		plot(Xm2,Ym2, color=colors[Bin], linestyle='dashed', lw=3)
		axvline(1,0,max(Ym1),color='black', lw=3)
		ax1.grid(True)
		l1=ax1.legend(["Mass 1","Mass 2"] ,title="Component ($m1 > m2$)")
		lb1 = Rectangle((0, 0), 1, 1, fc='black')
		lb2 = Rectangle((0, 0), 1, 1, fc='blue')
		lb3 = Rectangle((0, 0), 1, 1, fc='red')
		lb4 = Rectangle((0, 0), 1, 1, fc='green')
		l2=legend([lb1,lb2,lb3,lb4],["$1M_{\odot} - 1M_{\odot}$","$1.4M_{\odot} - 1.4M_{\odot}$","$1M_{\odot} - 2.5M_{\odot}$","$2.5M_{\odot} - 2.5M_{\odot}$"], loc='upper left', title="Neutron Star Masses")
		gca().add_artist(l1)
		xlabel('Component Masses ($M_{\odot}/M_{\odot}^{inject}$)', fontsize=18)
		title('Mass Posterior PDFs', fontsize=26)

#		mcMin = min(mc)
#		mcMax = max(mc)
#		dx = (mcMax- mcMin) / 1000.
#		n = mcMin

#		while n <= mcMax:
#			Xmc.append(n)
#			Ymc.append(float(mcKDE(n)))
#			n += dx

#		ax2 = subplot(4,1,2)
#		plot(Xmc,Ymc, color=colors[Bin], lw=1)
#		fill_between(Xmc,Ymc,zeros(len(Ymc)), alpha=0.4, color=colors[Bin])
#		axvline(1,0,max(Ymc),color='black', lw=3)
#		ax2.grid(True)
#		xlabel('Chirp Masses ($M_{\odot}/M_{\odot}^{inject}$)', fontsize=18)

		mMin = min(M)
		mMax = max(M)
		dx = (mMax - mMin) / 1000.
		n = mMin

		while n <= mMax:
			Xm.append(n)
			Ym.append(float(mKDE(n)))
			n += dx

		ax3 = subplot(3,1,2)
		plot(Xm,Ym, color=colors[Bin], lw=3)
		fill_between(Xm,Ym,zeros(len(Ym)), alpha=0.3, color=colors[Bin])
		axvline(1,0,max(Ym),color='black', lw=3)
		ax3.grid(True)
		ylabel('Probability Densities',fontsize=22)
		xlabel('Total Mass ($M_{\odot}/M_{\odot}^{inject}$)', fontsize=18)


		qMin = min(q)
		qMax = max(q)
		dx = (qMax - qMin) / 1000.
		n = qMin

		while n <= qMax:
			Xq.append(n)
			Yq.append(float(qKDE(n)))
			n += dx

		ax4 = subplot(3,1,3)
		plot(Xq,Yq, color=colors[Bin], lw=3)
		fill_between(Xq,Yq,zeros(len(Yq)), alpha=0.3, color=colors[Bin])
#		axvline(1,0,max(Yq),color='black', lw=3)
		ax4.grid(True)
		xlabel('Mass Ratios ($q$)', fontsize=18)

		Bin += 1


show()
