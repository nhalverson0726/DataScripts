#! python3
# tclCal.py finds relevant calbration data in file and strips
#all irrelevant data

import pyperclip
import re

text = pyperclip.paste() # pastes string from clipboard

pH1 = []
pH2 = []
pH3 = []
cond = []
step = []

dataRegex = re.compile(r'pH\sof\smixed\sT1:\s(\d{4,5}),\s(\d{4,5}),\s(\d{4,5})\spH\s\*\s1000\r')

condRegex = re.compile(r'Temp\sCorrected\sConductivity\sSamp\s\+\sT1:\s(\d*)')

stepRegex = re.compile(r'Mixing\s(\d{1,4})\ssteps\sof\sT1...')

text = text.split('\n') # splits pssted text into list, stores in data
                       
for i in range(len(text)):
    mo = dataRegex.search(text[i])
    if mo is not None:
##        print(mo.group())
##        print(mo.group(1))
##        print(mo.group(2))
##        print(mo.group(3))
        pH1.append(mo.group(1))
        pH2.append(mo.group(2))
        pH3.append(mo.group(3))
    mo2 = condRegex.search(text[i])
    if mo2 is not None:
        print(mo2.group(1))
        cond.append(mo2.group(1))
    mo3 = stepRegex.search(text[i])
    if mo3 is not None:
        step.append(mo3.group(1))

data = []

for i in range(len(pH1)):
    pH1[i] = int(pH1[i])/1000
    pH2[i] = int(pH2[i])/1000
    pH3[i] = int(pH3[i])/1000
    cond[i] = int(cond[i])/1000
    data.append(str(1+(i%2))+ '\t' + str(step[i]) + '\t' + str(cond[i]) + '\t' + str(pH1[i]) + '\t' + str(pH2[i]) + '\t' + str(pH3[i]) +'\n')
output = ''.join(data)
if type(output) == str and len(output)>0: # copies new string to cliipboard
    pyperclip.copy(output)
    print('Data ready to paste')
else:
    print('Something went wrong!')
    

