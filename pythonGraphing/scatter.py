# This program reads in a CSV of data with a descriptive header
# The specified columns are scattered against each other
# - Kyle Rocha-Brownell 2018, kyledbrownell@gmail.com

import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Column number of each dataset (column numbers start at 0)
columnA = 6
columnB = 8

# Read data from file #
with open('rtdIce2.CSV', 'rt') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    dataRaw = list(reader)
headers = dataRaw.pop(0)  # remove headers and save them
data = np.array(dataRaw, dtype=float)  # convert raw data to array

# Scatter all points from columns A and B #
fig, ax = plt.subplots()
plt.scatter(data[:,columnA], data[:,columnB])
plt.xlabel(headers[columnA])  # name axis from header
plt.ylabel(headers[columnB])  # name axis from header
ax.xaxis.set_major_locator(mpl.ticker.AutoLocator())
ax.yaxis.set_major_locator(mpl.ticker.AutoLocator())

plt.show()
