from mpl_toolkits.basemap import Basemap
import scipy.ndimage as ndimage
from matplotlib import pyplot as plt,cm as mpl_cm,lines as mpl_lines,colorbar

np.seterr(under='ignore')

myfig=plt.figure()
plt.clf()
m=Basemap(projection='moll',lon_0=0.0,lat_0=0.0)


m.drawmapboundary()
m.drawcoastlines(linewidth=0.5)
m.drawparallels(np.arange(-90.,90.,45.),labels=[1,0,0,0],labelstyle='+/-')
#m.fillcontinents(color='#cc9966',lake_color='#99ffff',alpha=0.7)
# draw parallels
m.drawmeridians(np.arange(0.,360.,90.),labels=[0,0,0,1],labelstyle='+/-')
# draw meridians
plt.title("Sky Location Uncertainty", fontsize=22) # add a title
m.drawmapboundary()
#colorbar.ColorbarBase.set_label(test,'$\log_{10}$($\Omega$)  $(deg)^2$', fontsize=15)

ra = []
dec= []
sa = []
deg= []
for prefix in ['2.5_2.5']:
#for prefix in ['1_1','1.4_1.4','1_2.5','2.5_2.5']:
	for run in range(1,41):
		filename = prefix + '/' + str(run) + '/post/ranked_sky_pixels.dat'
		try: 
			file = open(filename)
		except IOError:
			print "Warning, " + filename + " isn\' there"
			continue
		filedata = file.readlines()
		file.close()

		fileSummaryName = prefix + '/' + str(run) + '/post/summary_statistics.dat'
		try: 
			fileSummary = open(fileSummaryName)
		except IOError:
			print "Warning, " + filenameSummaryName + " isn\' there"
			continue
		fileSummaryData = fileSummary.readlines()
		fileSummary.close()
		gmst = float(fileSummaryData[31].split()[6])
		gmst = np.mod(gmst/3600.,24.)
		print gmst

		i = 0
		cum = float(filedata[1].split()[3]) 

		while cum <= 0.95: #two sigma
			cum = float(filedata[i+2].split()[3]) 
			ra.append(( - gmst + float(filedata[i+2].split()[1]))*0.26179938779)
			dec.append(float(filedata[i+2].split()[0])*0.01745329251)
			sa.append(28.)
			i += 1
		for j in range(i):
			deg.append(i*(41252.96129655765) / (len(filedata) - 1))

ra = np.array(ra)
dec= np.array(dec)
sa = np.array(sa)

ra_reverse =  ra*57.296

plx,ply=m(
	  ra_reverse,
	  (dec)*57.296
	  )

m.scatter(plx,ply,s=sa,c='gray',edgecolors='none',cmap=plt.cm.gist_rainbow,alpha=0.75)

ra = []
dec= []
sa = []
deg= []
for prefix in ['2.5_2.5']:
#for prefix in ['1_1','1.4_1.4','1_2.5','2.5_2.5']:
	for run in range(1,41):
		filename = prefix + '/' + str(run) + '/post/ranked_sky_pixels.dat'
		try: 
			file = open(filename)
		except IOError:
			continue
		filedata = file.readlines()
		file.close()

		fileSummaryName = prefix + '/' + str(run) + '/post/summary_statistics.dat'
		try: 
			fileSummary = open(fileSummaryName)
		except IOError:
			print "Warning, " + filenameSummaryName + " isn\' there"
			continue
		fileSummaryData = fileSummary.readlines()
		fileSummary.close()
		gmst = float(fileSummaryData[31].split()[6])
		gmst = gmst/3600.

		i = 0
		cum = float(filedata[1].split()[3]) 

		while cum <= 0.67: #one sigma
			cum = float(filedata[i+2].split()[3]) 
			ra.append(( - np.mod(gmst,24.) + float(filedata[i+2].split()[1]))*0.26179938779)
			dec.append(float(filedata[i+2].split()[0])*0.01745329251)
			sa.append(20)
			i += 1
#		while cum <= 0.9545: #two sigma
#			cum = float(filedata[i+2].split()[3]) 
#			ra.append(float(filedata[i+2].split()[1])*0.26179938779)
#			dec.append(float(filedata[i+2].split()[0])*0.01745329251)
#			sa.append(1.)
#			i += 1
		for j in range(i):
			deg.append(i*(41252.96129655765) / (len(filedata) - 1))

ra = np.array(ra)
dec= np.array(dec)
sa = np.array(sa)

ra_reverse = ra*57.296

plx,ply=m(
	  ra_reverse,
	  dec*57.296
	  )

m.scatter(plx,ply,s=sa,c=deg,edgecolors='none',cmap=plt.cm.gist_rainbow,alpha=1)
test2 = m.colorbar(location='bottom')
colorbar.ColorbarBase.set_label(test2,'$1\sigma$ Solid Angle $(deg)^2$', fontsize=15)


#m.contourf(plx,ply,data,cmap=mpl_cm.gist_rainbow,alpha=0.8,tri=True)
#ax = subplot(2,1,1)
#ax = subplot(2,1,2)
#m.drawmapboundary()
#m.drawcoastlines(linewidth=0.5)
#m.drawparallels(np.arange(-90.,90.,45.),labels=[1,0,0,0],labelstyle='+/-')
# draw parallels
#m.drawmeridians(np.arange(0.,360.,90.),labels=[0,0,0,1],labelstyle='+/-')
#m.scatter(plx,ply,s=60,c=per,alpha=0.8)
# draw meridians
#plt.title("Circularity", fontsize=22) # add a title
#test2 = m.colorbar(location='bottom')
#colorbar.ColorbarBase.set_label(test2,'Fraction in circularized 1$\sigma$', fontsize=15)

plt.draw()
plt.show()
