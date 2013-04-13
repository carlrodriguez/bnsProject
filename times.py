from matplotlib import pyplot as plt,cm as mpl_cm,lines as mpl_lines,colorbar

massBins = ["1_1","1.4_1.4","1_2.5","2.5_2.5"]
names=["$1M_{\odot} - 1M_{\odot}$","$1.4M_{\odot} - 1.4M_{\odot}$","$1M_{\odot} - 2.5M_{\odot}$","$2.5M_{\odot} - 2.5M_{\odot}$"]
times = [[] for i in range(4)]
i = 0

for mass in massBins:
	file = open(mass + '-times.dat')
	filedata = file.readlines()
	for j in range(len(filedata)):
		hrs,mins,secs = filedata[j].split(":")
		times[i].append(float(hrs) + float(mins)/60. + float(secs)/3600.)
	file.close()
	i += 1

ax = subplot(111)
ax.set_xlabel('Hours')
ax.set_ylabel('Number')
for i in range(4):
		ax1 = subplot(2,2,i+1)
		ax1.hist(times[i])
		title(names[i], fontsize = 18)

show()
