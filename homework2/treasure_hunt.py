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





