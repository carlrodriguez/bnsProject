from math import *
from numpy import *
from pylal import bayespputils as bppu

Dist= [[] for i in range(4)]
Iota= [[] for i in range(4)]
filenumbers = ['5','27','40','36']
injected = [(100.8422,1.5548),(124.73,1.782),(170.41,2.135),(145.78,1.671)]

for j in range(4):
		file = open('1.4_1.4/' + filenumbers[j] + '/post/posterior_samples.dat')
		filedata = file.readlines()
		file.close()

		for i in range(1,len(filedata)):
			[dist,chain,v1_end_time,f_lower,logll1,logl,loglh1,loglh2,v1h1_delay,l1v1_delay,l1h1_delay,loglv1,m1,ra,l1_end_time,m2,iota,v1l1_delay,psi,post,cycle,mc,h1v1_delay,logprior,phi_orb,h1l1_delay,q,prior,h1_end_time,eta,time,cosiota,dec] = filedata[i].split()
			Dist[j].append(float(dist))
			Iota[j].append(float(iota))


subplots_adjust(left=None, bottom=None, right=None, top=0.83, wspace=None, hspace=0.4)
for j in range(1,5):
		suptitle("2D Marginalized Distance/Inclination Posteriors", fontsize=26)
		subplot(2,2,j)
		#ax.set_xticks([1.3484,1.3486,1.3488, 1.3490,1.3492])
		gridsize = 60
		hexbin(Dist[j-1],Iota[j-1], gridsize=gridsize, cmap=cm.gist_stern, bins=None)
		plot(injected[j-1][0],injected[j-1][1],marker='o', color='w',markersize=18)
		pyplot.colorbar()
		title('$D$ vs. $\iota$',fontsize=24)
		xlabel('$D (mpc)$',fontsize=18)
		ylabel('$\iota (rad)$',fontsize=18)

draw()
show()
