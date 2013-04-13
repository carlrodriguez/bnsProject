from math import *
from numpy import *
from pylal import bayespputils as bppu

Mc = []
Eta = []
M1 = []
M2 = []

file = open('postSamp1414.dat')
filedata = file.readlines()
file.close()

for i in range(1,len(filedata)):
	[dist,chain,v1_end_time,f_lower,logll1,logl,loglh1,loglh2,v1h1_delay,l1v1_delay,l1h1_delay,loglv1,m1,ra,l1_end_time,m2,iota,v1l1_delay,psi,post,cycle,mc,h1v1_delay,logprior,phi_orb,h1l1_delay,q,prior,h1_end_time,eta,time,cosiota,dec] = filedata[i].split()
	Eta.append(float(eta))
	Mc.append(float(mc))
	M1.append(float(m1))
	M2.append(float(m2))


suptitle("2D Marginalized Mass Posteriors for $1.4M_{\odot}/1.4M_{\odot}$ System", fontsize=30)
ax = subplot(1,2,1)
#ax.set_xticks([1.3484,1.3486,1.3488, 1.3490,1.3492])
subplots_adjust(left=None, bottom=None, right=None, top=0.83, wspace=None, hspace=0.15)
gridsize = 60
hexbin(Mc,Eta, gridsize=gridsize, cmap=cm.gist_stern, bins=None)
title('$\mathcal{M}_c$ vs. $\eta$',fontsize=24)
xlabel('$\mathcal{M}_c$',fontsize=18)
ylabel('$\eta$',fontsize=18)
cb = pyplot.colorbar()
ax = subplot(1,2,2)
hexbin(M1,M2, gridsize=gridsize, cmap=cm.gist_stern, bins=None)
title('$M_1$ vs. $M_2$',fontsize=24)
xlabel('$M_1$',fontsize=18)
ylabel('$M_2$',fontsize=18)
cb = pyplot.colorbar()

draw()
show()
