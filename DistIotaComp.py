from math import *
from numpy import *

Dist= [[] for i in range(5)]
Iota= [[] for i in range(5)]
filenumbers = ['15','26','38','39']
#filenumbers = ['5','27','36']
injected = [(102.81124,1.67304),(119.14434,1.961056),(131.2679,0.9685463),(51.905911,1.489843)]
#injected = [(100.8422,1.5548),(124.73,1.782),(145.78,1.671)]

for j in range(4):
		file = open('HLVI/1.4_1.4/' + filenumbers[j] + '/post/posterior_samples.dat')
		filedata = file.readlines()
		file.close()

		for i in range(100,len(filedata)):
			[dist,chain,v1_end_time,f_lower,logll1,logl,loglh1,v1h1_delay,l1v1_delay,l1h1_delay,loglv1,m1,ra,l1_end_time,m2,iota,v1l1_delay,psi,post,cycle,mc,h1v1_delay,logprior,phi_orb,h1l1_delay,q,prior,h1_end_time,eta,li1,time,cosiota,dec] = filedata[i].split()
			Dist[j].append(float(dist))
			Iota[j].append(float(iota))


subplots_adjust(left=0.15, bottom=None, right=None, top=0.92, wspace=None, hspace=0.5)
suptitle("Distance/Inclination PDFs", fontsize=20)
for j in range(1,5):
		subplot(4,1,j)
		#ax.set_xticks([1.3484,1.3486,1.3488, 1.3490,1.3492])
		gridsize = 60
		hexbin(Dist[j-1],Iota[j-1], gridsize=gridsize, cmap=cm.gist_stern, bins=None)
		plot(injected[j-1][0],injected[j-1][1],marker='o', color='w',markersize=18)
		pyplot.colorbar()
		title('$D$ vs. $\iota$',fontsize=16)
		xlabel('Distance (MPC)',fontsize=12)
		ylabel('Inclination (rad)',fontsize=12)

draw()
show()
