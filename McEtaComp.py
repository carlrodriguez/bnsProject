from math import *
from numpy import *

Mc = []
Q = []
M1 = []
M2 = []

file = open('postSamp125.dat')
filedata = file.readlines()
file.close()

for i in range(1,len(filedata)):
	[dist,chain,v1_end_time,f_lower,logll1,logl,loglh1,loglh2,v1h1_delay,l1v1_delay,l1h1_delay,loglv1,m1,ra,l1_end_time,m2,iota,v1l1_delay,psi,post,cycle,mc,h1v1_delay,logprior,phi_orb,h1l1_delay,q,prior,h1_end_time,eta,time,cosiota,dec] = filedata[i].split()
	Q.append(float(q))
	Mc.append(float(mc))
	M1.append(float(m1))
	M2.append(float(m2))


suptitle("Mass PDFs for $1M_{\odot}/2.5M_{\odot}$ System", fontsize=20)
subplots_adjust(left=None, bottom=None, right=None, top=None,
                  wspace=None, hspace=1)
ax = subplot(2,1,1)
ax.set_xticks([1.3484,1.3486,1.3488, 1.3490,1.3492])
subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.3)
gridsize = 60
hexbin(Mc,Q, gridsize=gridsize, cmap=cm.gist_stern, bins=None)
plot(1.348809,0.4,marker='o', color='w',markersize=18)
title('$\mathcal{M}_c$ vs. $q$',fontsize=16)
xlabel('$\mathcal{M}_c$ $(M_{\odot})$', fontsize=14)
ylabel('$q$', fontsize=14)
cb = pyplot.colorbar()
ax = subplot(2,1,2)
hexbin(M1,M2, gridsize=gridsize, cmap=cm.gist_stern, bins=None)
plot(2.5,1.,marker='o', color='w',markersize=18)
title('$M_1$ vs. $M_2$',fontsize=16)
xlabel('$M_1$ $(M_{\odot})$',fontsize=14)
ylabel('$M_2$ $(M_{\odot})$',fontsize=14)
cb = pyplot.colorbar()

draw()
show()
