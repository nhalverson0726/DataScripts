#! python3
# tclCal.py finds relevant calbration data in file and strips
#all irrelevant data

import pyperclip
import re

text = pyperclip.paste() # pastes string from clipboard
data = []
text = text.split('\n') # splits pssted text into list, stores in data

for i in range(len(text)): # finds the relevent ddata line in text file, adds it to data variable
    if 'TCL' and 'nA * 1000' in text[i]:
        data.append(text[i])
        
dataRegex = re.compile(r'(-)?\d+')
                       
for i in range(len(data)): # strips non integer values from each entry in the data list
    mo = dataRegex.search(data[i])
    data [i] = mo.group()

    
del data[::2] # deletes every other value in data list,
# becasue they are duplicates
        
output = '\n'.join(data) #Turns list into a string formatted to paste into excel

if type(output) == str and len(output)>0: # copies new string to cliipboard
    pyperclip.copy(output)
    print('Data ready to paste')
else:
    print('something went wrong')
    

