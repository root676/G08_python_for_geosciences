#-------------------------------------------------------------------------------
# Name:        treasure_hunt.py
# Purpose:     this routine helps to find the treasure
#
# Authors:     Stefan Fnord, Clemens Raffler, Daniel Zamojski
#
# Created:     29.05.2015
# Copyright:   (c) Stefan Fnord, Clemens Raffler, Daniel Zamojski 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


import csv
import urllib2
import netCDF4

import numpy as np
import matplotlib.pyplot as plt

download_page = "http://rs.geo.tuwien.ac.at/downloads/cpa/"



# It has 4 legs but cannot walk.
filename1 = "table"
response = urllib2.urlopen(download_page+filename1+".csv")



# Young I?m tall, old I?m short, I love to glow, breath is my foe.
column1 = "candle"


# load header from file
for idx,elem in enumerate(response.readline()[:-1].split(',')):
    # if answer of last question is in the header, then query the data
    if elem==column1:
        break

else:
    print column1+" not found in header of the file - check the last question"
    exit


# load data from file
clue1_array = np.loadtxt(response,skiprows=0, delimiter=',')
del response

# What digit is the most frequent between the numbers 1 and 1000?
thousandlist = range(1,1001)
digitlist =[]
for element in thousandlist:
    for digit in str(element):
        digitlist.append(int(digit))

onetothousand_vector = np.array(digitlist)

plt.hist(onetothousand_vector, bins=10)
plt.show()

# TODO - hier noch aus dem histogramm bzw aus array die h?ufigste Zahl berechen
# und an row1 uebergeben!
row1 = 1

# read from file (row1-1 because without header)
filename2part1 = clue1_array[row1-1][idx]
if filename2part1==int(filename2part1):
    filename2part1 = int(filename2part1)

# Stay hungry, stay ......, Steve Jobs
filename2part2 = "foolish"

# download file
print download_page+str(filename2part1)+'_'+filename2part2+'.nc'

nc = netCDF4.Dataset(download_page+str(filename2part1)+'_'+filename2part2+'.nc')
print nc
#response = urllib2.urlopen(download_page+filename2part1+'_'+filename2part2+'.nc')

