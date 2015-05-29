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



download_page = "http://rs.geo.tuwien.ac.at/downloads/cpa/"



# It has 4 legs but cannot walk.
q1 = "table"





response = urllib2.urlopen(download_page+q1+".csv")

g = response.readlines()

#cr = csv.reader(response)

#for row in cr:
#    print row



# Young I?m tall, old I?m short, I love to glow, breath is my foe.
q2 = "candle"


# What digit is the most frequent between the numbers 1 and 1000?
q3 = ""





