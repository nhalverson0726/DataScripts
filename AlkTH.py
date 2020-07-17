import os, csv, math
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


os.chdir(r'C:\Users\e-sens\Documents')

dataFile = open('alkTHCorrelations.csv')
dataReader = csv.reader(dataFile)
data = list(dataReader)
del data[0]

## turn string numbers into int

for i in range(len(data)):
    for k in range(2):
        data[i][k] = float(data[i][k])

arr = np.array(data) # make array

def linRegress(arr): # input is (n x 2) array
    import numpy as np
    import math
    from scipy import stats
    
    ysubi = arr[:,1] # y points from table
    xsubi = arr[:,0] # x points from table
    n = len(arr) # number of intances
    dof = n-2 # fot fit where intercept is not forced though origin

    t95 = [1.96, 12.706, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306,
          2.262, 2.228, 2.201, 2.179, 2.16, 2.145, 2.131, 2.12, 2.11,
          2.101, 2.093, 2.086, 2.08, 2.074, 2.069, 2.064, 2.06,
          2.056, 2.052, 2.048, 2.045, 2.042]
    ## t table for 95 percent confidence, two tails. t95[0] is inf number of points

    # find slope and int

    slope, intercept, r_value, p_value, std_err = stats.linregress(arr)

    yhat = (slope*xsubi) + intercept  # y fit from xsubi

    rss = np.sum(np.square(ysubi - yhat)) # residual sum of squares

    ssuby2 = rss/dof # variance of y values

    stdy = math.sqrt(ssuby2)

    e95 = stdy * t95[dof]

    return slope, intercept, stdy, e95

slope, intercept, stdy, e95 = linRegress(arr)

print('Error in y-fit = ' + str(e95))
print('Slope:' + str(slope))
print('Intercept:' + str(intercept))




