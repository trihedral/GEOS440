# This program reads in a CSV of data with a descriptive header
# Columns 0-5 are taken to be yyyy, mm, dd, hh, mm, ss
# All remaining columns are graphed as different data series
# - Kyle Rocha-Brownell 2018, kyledbrownell@gmail.com

import csv
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt


# Read data from file #
with open('cooling2.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    dataRaw = list(reader)
headers = dataRaw.pop(0)  # remove headers and save them
data = np.array(dataRaw, dtype=float)  # convert raw data to numeric array
num = len(data[:,0]);

# Create datetime list from columns 0-5 (yrs-secs) #
dtList = []
for i in range (0, num):
    dtList.append( dt.datetime( 
            int(data[i,0]),int(data[i,1]),int(data[i,2]),
            int(data[i,3]),int(data[i,4]),int(data[i,5]) 
    ) )
    
# Plot sets vs time #
plt.plot(dtList, data[:,6], label=headers[6])

plt.show()
