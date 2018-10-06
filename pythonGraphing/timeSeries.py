# This program reads in a CSV of data with a descriptive header
# Columns 0-5 are taken to be yyyy, mm, dd, hh, mm, ss
# All remaining columns are graphed as different data series
# - Kyle Rocha-Brownell 2017, kyledbrownell@gmail.com

import csv
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib as mpl
'''
# Axis names
xAxisLabel = "Amazing X-Axis, blah, blah"
yAxisLabel = "Neato Y-Axis Label"
# Number of Y-axis minor ticks per major ticks
yMinorPerMajorTicks = 10
# X-Axis minor tick options are: YearLocator, MonthLocator, etc.
#xMinorTicks = mpl.dates.MinuteLocator()
# Date formatting options are: %Y %m %d %H %M %S
xFmt = mpl.dates.DateFormatter('%H:%M')
# Legend location options are 0-5
legendLocation = 2
# Note 1: Series names for the legend are taken from the CSV header
# Note 2: Major axis ticks are decided automagically by python
'''
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

# Plot sets vs time #
fig, ax = plt.subplots()
plt.plot(dtList, data[:,6], label=headers[6])
'''
fig, ax = plt.subplots()
for i in range (6, len(data[1,:])):
    plt.plot(dtList, data[:,i], label=headers[i])
'''
# Format Axes #
'''
plt.xlabel(xAxisLabel)
plt.ylabel(yAxisLabel)
plt.legend(loc = legendLocation)    # 0-5
ax.xaxis.set_major_formatter(xFmt)
try:
    ax.xaxis.set_minor_locator(xMinorTicks)
except:
    None

ax.tick_params(axis='both',which='major',length=6)
ax.tick_params(axis='both',which='minor',length=4)
ax.yaxis.set_minor_locator(
    mpl.ticker.AutoMinorLocator(n=yMinorPerMajorTicks));
fig.autofmt_xdate()'''

plt.show()
