import csv
import numpy as np
import os
import matplotlib.pyplot as plt

os.chdir("C:\\Users\\e-sens\\Downloads")
spyFile = open("SPY.csv")
spyReader = csv.reader(spyFile)
spyData = list(spyReader)
del spyData[0]
high = []
day = []
low = []
gp = []
date = []
gap = 0.02

for i in range(len(spyData)-1):
    if (float(spyData[i+1][1]) - float(spyData[i][4])) / float(spyData[i][4]) > gap:
        print(' | '.join(spyData[i]))
        print(' | '.join(spyData[i+1]))
        print('gap overnight: ' + str((float(spyData[i+1][1]) - float(spyData[i][4])) / float(spyData[i][4])))
        print('percent gain open to high:  ' + str((float(spyData[i+1][2]) - float(spyData[i+1][1]))/ float(spyData[i+1][1])))
        print('percent loss open to low: ' + str((float(spyData[i+1][3]) - float(spyData[i+1][1]))/ float(spyData[i+1][1])))
        print('percent change over day: ' + str((float(spyData[i+1][4]) - float(spyData[i+1][1]))/ float(spyData[i+1][1])))
        print('\n')
        high.append((float(spyData[i+1][2]) - float(spyData[i+1][1]))/ float(spyData[i+1][1]))
        low.append((float(spyData[i+1][3]) - float(spyData[i+1][1]))/ float(spyData[i+1][1]))
        day.append((float(spyData[i+1][4]) - float(spyData[i+1][1]))/ float(spyData[i+1][1]))
        gp.append((float(spyData[i+1][1]) - float(spyData[i][4])) / float(spyData[i][4]))
        date.append(spyData[i+1][0])
        
h = np.array(high)
l = np.array(low)
d = np.array(day)
g = np.array(gp)
t = np.array(date)

##plt.hist(h, density=False, bins=30) 
##
##plt.ylabel('Counts')
##plt.title('gain to high')
##plt.show()

##plt.hist(l, density=False, bins=30) 
##
##plt.ylabel('Counts')
##plt.title('loss to low')
##plt.show()
##
##plt.hist(d, density=False, bins=30) 
##
##plt.ylabel('Counts')
##plt.title('day change')
##plt.show()

print('change\tmedian\taverage\tmin\tmax')
print('day:\t%.4f\t%.4f\t%.4f\t%.4f' % (np.median(d), np.average(d), np.amin(d), np.amax(d)))
print('high:\t%.4f\t%.4f\t%.4f\t%.4f' % (np.median(h), np.average(h), np.amin(h), np.amax(h)))
print('low:\t%.4f\t%.4f\t%.4f\t%.4f' % (np.median(l), np.average(l), np.amin(l), np.amax(l)))
print('\nn=\t' +str(len(h)))
print('Gap:\t%.2f' % gap)


data = np.vstack((t,g,d,h,l))
data = np.transpose(data)
np.savetxt("spyData0.02.csv", data, delimiter=",", fmt='%s', header='date,gap,day,high,low')


