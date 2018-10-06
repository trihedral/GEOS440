#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 11:33:22 2018

@author: kyle
"""

import csv

csvfile = open("LOG000.CSV", "rt")            # load file into memory
reader = csv.reader(csvfile, delimiter=",")   # parse file for values
dataRaw = list(reader)                        # convert to 2D list (array)

headers = dataRaw.pop(0)           # remove top row (headers) from data


print (headers)
print(dataRaw[0][1])
