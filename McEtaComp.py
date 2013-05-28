from math import *
from numpy import *

Mc = []
Q = []
M1 = []
M2 = []

file = open('HLVI/1.4_1.4/10/post/posterior_samples.dat')
filedata = file.readlines()
file.close()

for i in range(1,len(filedata)):
	[dist,chain,v1_end_time,f_lower,logll1,logl,loglh1,v1h1_delay,l1v1_delay,l1h1_delay,loglv1,m1,ra,l1_end_time,m2,iota,v1l1_delay,psi,post,cycle,mc,h1v1_delay,logprior,phi_orb,h1l1_delay,q,prior,h1_end_time,eta,li1,time,cosiota,dec] = filedata[i].split()
	Q.append(float(q))
	Mc.append(float(mc))
	M1.append(float(m1))
	M2.append(float(m2))


suptitle("Mass PDFs for $1.4M_{\odot}/1.4M_{\odot}$ System", fontsize=20)
subplots_adjust(left=0.15, bottom=None, right=None, top=0.88, wspace=None, hspace=0.5)
ax = subplot(2,1,1)
#ax.set_xticks([1.3484,1.3486,1.3488, 1.3490,1.3492])
ax.set_xticks([1.2185,1.2186,1.2187, 1.2188,1.2189])
subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.3)
gridsize = 60
hexbin(Mc,Q, gridsize=gridsize, cmap=cm.gist_stern, bins=None)
#plot(1.348809,0.4,marker='o', color='w',markersize=18)
plot(1.21877,1,marker='o', color='w',markersize=18)
title('$\mathcal{M}_c$ vs. $q$',fontsize=16)
xlabel('Chirp Mass $(M_{\odot})$', fontsize=12)
ylabel('Mass Ratio', fontsize=12)
cb = pyplot.colorbar()
ax = subplot(2,1,2)
hexbin(M1,M2, gridsize=gridsize, cmap=cm.gist_stern, bins=None)
plot(1.4,1.4,marker='o', color='w',markersize=18)
title('$M_1$ vs. $M_2$',fontsize=16)
xlabel('Mass 1 $(M_{\odot})$',fontsize=12)
ylabel('Mass 2 $(M_{\odot})$',fontsize=12)
cb = pyplot.colorbar()

draw()
show()
