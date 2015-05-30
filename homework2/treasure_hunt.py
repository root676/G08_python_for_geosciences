#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dan
#
# Created:     29.05.2015
# Copyright:   (c) Dan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python



import csv
import urllib2

import numpy as np
import matplotlib.pyplot as plt



download_page = "http://rs.geo.tuwien.ac.at/downloads/cpa/"



# It has 4 legs but cannot walk.
q1 = "table"
response = urllib2.urlopen(download_page+q1+".csv")

# Young I?m tall, old I?m short, I love to glow, breath is my foe.
q2 = "candle"

clue1_array = np.loadtxt(response,skiprows=1, delimiter=',')
del response
filename2part1 = str(clue1_array[0,1])
print filename2part1




# What digit is the most frequent between the numbers 1 and 1000?
#mir fiel keine Numpy Lösung ein...
thousandlist = range(1,1001)
digitlist =[]
for element in thousandlist:
    for digit in str(element):
        digitlist.append(int(digit))

onetothousand_vector = np.array(digitlist)

plt.hist(onetothousand_vector, bins=10)
plt.show()

q3 = 1

# Stay hungry, stay ......, Steve Jobs
q4 = "foolish"

response = urllib.urlopen(download_page+q1+"_"+q4+".nc")


