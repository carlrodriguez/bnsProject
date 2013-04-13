from mpl_toolkits.basemap import Basemap
from matplotlib import pyplot as plt,cm as mpl_cm,lines as mpl_lines,colorbar

np.seterr(under='ignore')

myfig=plt.figure()
plt.clf()
m=Basemap(projection='moll',lon_0=0.0,lat_0=0.0)

file = open('SolidAngles_2.5_2.5.dat')
filedata = file.readlines()
file.close()

ra = []
dec= []
sa = []
per= []
for i in range(1,len(filedata)):
	ra.append(float(filedata[i].split()[0]))
	dec.append(float(filedata[i].split()[1]))
	sa.append(float(filedata[i].split()[2]))
	per.append(float(filedata[i].split()[3])/100.)

ra = np.array(ra)
dec= np.array(dec)

ra_reverse = 2*pi - ra*57.296

plx,ply=m(
          ra_reverse,
          dec*57.296
          )

#m.contourf(plx,ply,data,cmap=mpl_cm.jet,alpha=0.8,tri=True)
#ax = subplot(2,1,1)
m.drawmapboundary()
m.drawcoastlines(linewidth=0.5)
m.drawparallels(np.arange(-90.,90.,45.),labels=[1,0,0,0],labelstyle='+/-')
# draw parallels
m.drawmeridians(np.arange(0.,360.,90.),labels=[0,0,0,1],labelstyle='+/-')
m.scatter(plx,ply,s=60,c=log10(sa),alpha=0.8)
# draw meridians
plt.title("Sky Location Uncertainty", fontsize=22) # add a title
test = m.colorbar(location='bottom')
colorbar.ColorbarBase.set_label(test,'$\log_{10}$($\Omega$)  $(deg)^2$', fontsize=15)
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
