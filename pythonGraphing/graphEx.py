# This program reads in a CSV of data with a descriptive header
# Columns 0-5 are taken to be yyyy, mm, dd, hh, mm, ss
# Remaining columns can be graphed as different data series
# - Kyle Rocha-Brownell 2018, kyledbrownell@gmail.com

import csv
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib as mpl
from   scipy.optimize import curve_fit

def exp_func(t, dT, tau, Tf):
    return dT*np.exp(-t/tau)+Tf

# Read data from file #
with open('cooling2.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    dataRaw = list(reader)
headers = dataRaw.pop(0)  # remove headers and save them
data = np.array(dataRaw, dtype=float)  # convert raw data to numeric array
num = len(data[:,0])

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


# Curve Fit #
seconds = np.empty(num)
for i in range(0, num):
    seconds[i] = (dtList[i].timestamp() - dtList[0].timestamp())
fitParam, fitCov = curve_fit(exp_func, seconds, data[:,6])
expY = exp_func(seconds, fitParam[0], fitParam[1], fitParam[2] )
plt.plot(dtList, expY, label="Exponential Fit")

print( "Delta T: " + str(fitParam[0]) )
print( "Time Constant: " + str(fitParam[1]) )
print( "Final Temp: " + str(fitParam[2]) )
std = np.sqrt(np.diag(fitCov))
print( "Delta T Standard Deviation: " + str(std[0]) )
print( "Time Constant Standard Deviation: " + str(std[1]) )
print( "Final Temp Standard Deviation: " + str(std[2]) )

# Set labels #
plt.title("Title")
plt.xlabel("xAxis")
plt.ylabel("yAxis")
plt.legend(loc = 0)

# Format axes #
xFmt = mpl.dates.DateFormatter('%M:%S') # %Y %m %d %H %M %S
ax.xaxis.set_major_formatter(xFmt)
fig.autofmt_xdate()  # puts date labels at angle

plt.show()
