# This program reads in a CSV of data with a descriptive header
# Columns 0-5 are taken to be yyyy, mm, dd, hh, mm, ss
# All remaining columns are graphed as different data series
# - Kyle Rocha-Brownell 2018, kyledbrownell@gmail.com

import csv
import numpy as np
import datetime as dt
import matplotlib as mpl
import matplotlib.pyplot as plt
from   scipy.optimize import curve_fit

def exponenial_func(t, a, b, c):
    return a*np.exp(-t/b)+c


# Read data from file #
with open('cooling2.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    dataRaw = list(reader)
headers = dataRaw.pop(0)               # remove headers and save them
data = np.array(dataRaw, dtype=float)  # convert raw data to numeric array
num = len(data[:,0]);                  # number of data points

# Create datetime list from columns 0-5 (yrs-secs) #
dtList = []
for i in range (0, num):
    dtList.append( dt.datetime( 
            int(data[i,0]),int(data[i,1]),int(data[i,2]),
            int(data[i,3]),int(data[i,4]),int(data[i,5]) 
    ) )
    
# Plot sets vs time #
fig, ax = plt.subplots()
plt.plot(dtList, data[:,6], label=headers[6])
plt.plot((dtList[0], dtList[num-1]), (0,0), "g--", label="0 Degrees C", )

# Create best-fit #
seconds = np.empty(num)
for i in range(0, num):
    seconds[i] = ( dtList[i].timestamp() - dtList[0].timestamp() )
fit_params, fit_cov = curve_fit( exponenial_func, seconds, data[:,6] )
expY = exponenial_func(seconds, fit_params[0], fit_params[1], fit_params[2])
plt.plot(dtList, expY, label="Exponential Fit")

# Set labels #
plt.title("Title")
plt.xlabel("xAxisLabel")
plt.ylabel("yAxisLabel")
plt.legend(loc = 0)    # 0-5 (0 = automatic)

# Format Axes #
xFmt = mpl.dates.DateFormatter('%M:%S') # %Y %m %d %H %M %S
ax.xaxis.set_major_formatter(xFmt)
#ax.xaxis.set_major_locator(mpl.ticker.AutoLocator())
#ax.yaxis.set_major_locator(mpl.ticker.AutoLocator())
fig.autofmt_xdate()

plt.show()
