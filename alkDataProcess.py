#! python3
# alkDataProcess.py finds endpopint using various methods (n x 4) input

import pyperclip, re
import numpy as np
from scipy import stats

input = pyperclip.paste() # pastes string from clipboard

stepsSample = 4320 # stesp sample on box

## formats input intoo list of lines
input  = input.split('\r\n')
input.remove('')

## REGEX format
dataRegex = re.compile(r'(\d{1,3})\t(\d{1,2}\.?\d{0,3})\t(\d{1,2}\.?\d{0,3})\t(\d{1,2}\.?\d{0,3})')

## find valkues for x and y axes
steps = []
pH1 = []
pH2 = []
pH3 = []

for i in range(len(input)):
    print(input[i])
    mo = dataRegex.search(input[i])
    steps.append(float(mo.group(1)))
    pH1.append(float(mo.group(2)))
    pH2.append(float(mo.group(3)))
    pH3.append(float(mo.group(4)))

# create 3 arrayas from x and y values
s = np.array(steps)
p1 = np.array(pH1)
p2 = np.array(pH2)
p3 = np.array(pH3)

## Format arrays
d1 = np.expand_dims(p1, axis=1)
d2 = np.expand_dims(p2, axis=1)
d3 = np.expand_dims(p3, axis=1)
s1 = np.expand_dims(s, axis=1)
    
h1 = np.hstack((s1, d1))
h2 = np.hstack((s1, d2))
h3 = np.hstack((s1, d3))

# pick points between 6.3 amd 4.9

g1 = h1[(h1[:,1] > 4.9) & (h1[:,1] < 6.3)]
g2 = h2[(h2[:,1] > 4.9) & (h2[:,1] < 6.3)]
g3 = h3[(h3[:,1] > 4.9) & (h3[:,1] < 6.3)]


## pick points below 4.1
l1 = h1[h1[:,1] < 4.1]
l2 = h2[h2[:,1] < 4.1]
l3 = h3[h3[:,1] < 4.1]

# pic points between 4.1 and 4.9

e1 = h1[(h1[:,1] >= 4.1) & (h1[:, 1] <= 4.9)]
e2 = h2[(h2[:,1] >= 4.1) & (h2[:, 1] <= 4.9)]
e3 = h3[(h3[:,1] >= 4.1) & (h3[:, 1] <= 4.9)]

# math for gran function 

g1[:,1] = g1[:,0] * np.power(10,g1[:,1])
g2[:,1] = g2[:,0] * np.power(10,g2[:,1])
g3[:,1] = g3[:,0] * np.power(10,g3[:,1])

l1[:,1] = (l1[:,0] + stepsSample) * np.power(10, np.negative(l1[:,1]))
l2[:,1] = (l2[:,0] + stepsSample) * np.power(10, np.negative(l2[:,1]))
l3[:,1] = (l3[:,0] + stepsSample) * np.power(10, np.negative(l3[:,1]))

# creates lists of gran arrays

g = [g1, g2 ,g3]
l = [l1, l2, l3]
e = [e1, e2, e3]

# creates dictonary for all the methods of finding endopoint


gepbc = {1 : '#N/A', 2 : '#N/A', 3 : '#N/A'}
lepbc = {1 : '#N/A', 2 : '#N/A', 3 : '#N/A'}
eep = {1 : '#N/A', 2 : '#N/A', 3 : '#N/A'}
gepwc = {1 : '#N/A', 2 : '#N/A', 3 : '#N/A'}
lepwc = {1 : '#N/A', 2 : '#N/A', 3 : '#N/A'}

# find endpoints from gran funcctions and add to dictionary

for i in range(3):
    if len(g[i]) == 2:
        slope, intercept, r_value, p_value, std_err = stats.linregress(g[i][:,0],g[i][:,1])
        endpoint = -intercept/slope
        gepwc[i+1] = int(endpoint)
        gepbc[i+1] = int(endpoint)     
    if len(g[i]) > 2:
        arr = g[i][:2, :]               # gets worst two points in array
        slope, intercept, r_value, p_value, std_err = stats.linregress(arr[:,0], arr[:,1])
        endpoint = -intercept/slope
        gepwc[i+1] = int(endpoint)
        arr = np.flipud(g[i])
        arr = arr[:2,:]
        slope, intercept, r_value, p_value, std_err = stats.linregress(arr[:,0], arr[:,1])
        endpoint = -intercept/slope
        gepbc[i+1] = int(endpoint)
    if len(l[i]) == 2:
        slope, intercept, r_value, p_value, std_err = stats.linregress(l[i][:,0], l[i][:,1])
        endpoint = -intercept/slope
        lepwc[i+1] = int(endpoint)
        lepbc[i+1] = int(endpoint)        
    if len(l[i]) > 2:
        arr = np.flipud(l[i])           # gets worst 2 points in arrray
        arr = arr[:2, :]                # gets worst 2 points in array
        slope, intercept, r_value, p_value, std_err = stats.linregress(arr[:,0], arr[:,1])
        endpoint = -intercept/slope
        lepwc[i+1] = int(endpoint)
        arr = l[i][:2,:]
        slope, intercept, r_value, p_value, std_err = stats.linregress(arr[:,0], arr[:,1])
        endpoint = -intercept/slope
        lepbc[i+1] = int(endpoint)      
    if len(e[i]) == 1:
        endpoint = e[i][0,0]
        eep[i+1] = int(endpoint)
    if len(e[i]) > 1:
        endpoint = np.average(e[i][:,0])
        eep[i+1] = int(endpoint)
    

sen1 = []
sen2 = []
sen3 = []

print('\t', 'GEPBC', '\t', 'GEPWC', '\t', 'EEP','\t', 'LEPBC', '\t', 'LEPWC')

data  = ['GEPBC\tGEPWC\tEEP\tLEPBC\tLEPWC\n']

for i in range(3):
    print('pH' + str(i+1),'\t', gepbc[i+1], '\t', gepwc[i+1], '\t', eep[i+1], '\t', lepbc[i+1], '\t', lepwc[i+1])
    data.append(str(gepbc[i+1]))
    data.append('\t')
    data.append(str(gepwc[i+1]))
    data.append('\t')
    data.append(str(eep[i+1]))
    data.append('\t')
    data.append(str(lepbc[i+1]))
    data.append('\t')
    data.append(str(lepwc[i+1]))
    data.append('\n')
    
output = ''.join(data)
pyperclip.copy(output)
print('\ndone.')
