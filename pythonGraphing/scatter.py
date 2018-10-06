# This program reads in a CSV of data with a descriptive header
# The specified columns are scattered against each other
# - Kyle Rocha-Brownell 2017, kyledbrownell@gmail.com

import csv
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib as mpl

# Column number of each dataset (column numbers start at 0)
columnA = 6
columnB = 7;  
# Number of minor ticks per major ticks
yMinorPerMajorTicks = 5
xMinorPerMajorTicks = 10
# Note: Axis labels are taken from the CSV header

# Read data from file #
with open('LOG000.CSV', 'rt') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    dataRaw = list(reader)
headers = dataRaw.pop(0)  # remove headers and save them
data = np.array(dataRaw)  # convert raw data to array

# Create datetime list from columns 0-5 (yrs-secs) #
dtList = []
for i in range (0, len(data[:,0])):
    dtList.append( dt.datetime( int(data[i,0]),int(data[i,1]),int(data[i,2]),int(data[i,3]),int(data[i,4]),int(data[i,5]) ) )

# Scatter all points from columns A and B #
fig, ax = plt.subplots()
plt.scatter(data[:,columnA], data[:,columnB])
plt.xlabel(headers[columnA])  # name axis from header
plt.ylabel(headers[columnB])  # name axis from header
ax.tick_params(axis='both',which='major',length=6)
ax.tick_params(axis='both',which='minor',length=4)
ax.xaxis.set_minor_locator(
    mpl.ticker.AutoMinorLocator(n=xMinorPerMajorTicks));
ax.yaxis.set_minor_locator(
    mpl.ticker.AutoMinorLocator(n=yMinorPerMajorTicks));
    
plt.show()
