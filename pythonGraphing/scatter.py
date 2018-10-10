# This program reads in a CSV of data with a descriptive header
# The specified columns are scattered against each other
# - Kyle Rocha-Brownell 2018, kyledbrownell@gmail.com

import csv
import numpy as np
import matplotlib.pyplot as plt

# Read data from file #
with open('rtdIce2.CSV', 'rt') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    dataRaw = list(reader)
headers = dataRaw.pop(0)               # remove headers and save them
data = np.array(dataRaw, dtype=float)  # convert raw data to array

plt.scatter(data[:,6], data[:,8])
plt.xlabel(headers[6])  # name axis from header
plt.ylabel(headers[8])  # name axis from header
plt.show()
