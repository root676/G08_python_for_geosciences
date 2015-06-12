#-------------------------------------------------------------------------------
# Name:        treasure_hunt.py
# Purpose:     this routine helps to find the treasure
#
# Authors:     Stefan Fleck, Clemens Raffler, Daniel Zamojski
#
# Created:     29.05.2015
# Copyright:   (c) Stefan Fnord, Clemens Raffler, Daniel Zamojski 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


import csv
import urllib2
import os
import netCDF4
from netCDF4 import Dataset

import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Required for NetCDF basemap plot
from mpl_toolkits.basemap import Basemap
import matplotlib
import h5py

import pandas as pd

download_page = "http://rs.geo.tuwien.ac.at/downloads/cpa/"


# It has 4 legs but cannot walk.
filename1 = "table"
response = urllib2.urlopen(download_page+filename1+".csv")


# Young I?m tall, old I?m short, I love to glow, breath is my foe.
column1 = "candle"


# read header from file
header1 = response.readline()[:-1].split(',')


# load header from file
for idx,elem in enumerate(header1):
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

data = Counter(onetothousand_vector)
row1 = data.most_common(1)[0][0]

# read from file (row1-1 because without header)
filename2part1 = clue1_array[row1-1][idx]
if filename2part1==int(filename2part1):
    filename2part1 = int(filename2part1)

# Stay hungry, stay ......, Steve Jobs
filename2part2 = "foolish"

# download file
url = str(download_page+str(filename2part1)+'_'+str(filename2part2)+'.nc')
print "Downloading: " + url

f = urllib2.urlopen (url)
with open(os.path.basename(url), "wb") as local_file:
          local_file.write(f.read())
nc = netCDF4.Dataset('9_foolish.nc')

lats = nc.variables['lat'][:]
lons = nc.variables['lon'][:]
force = nc.variables['force'][:]

lon_0 = lons.mean()
lat_0 = lats.mean()

m = Basemap(projection='mill', lat_0=0, lon_0=0,
              resolution='l', area_thresh=1000.0)

#%%

lon, lat = np.meshgrid(lons, lats)
xi, yi = m(lon, lat)

m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)
m.drawcoastlines()
m.drawstates()
m.drawcountries()

z = np.ma.array(force, mask= force==0)
cmap = matplotlib.colors.ListedColormap(['red'])

cs = m.pcolor(xi,yi,z, cmap = cmap)
plt.show()



capitalcity = "canberra"

# What planet has the shortest year?
filename3_part2 = "mercury"
filename3 =capitalcity +'_'+filename3_part2+'.npz'

#response = requests.get('C:\Users\Dan\Downloads\canberra_mercury.npz', stream=True)
#response = urllib2.urlopen(filename3,'wb')


url = download_page+filename3
print "Downloading: " + url

f = urllib2.urlopen(url)
with open(os.path.basename(url), "wb") as local_file:
          local_file.write(f.read())

# load data  TODO: download data; DANIEL: WORKING HERE
data = np.load('canberra_mercury.npz')

# gives back all available meta data
#data.files

# I?ll be . . . ., Arnold Schwarzenegger
variable3 = "back"

# giving back the data of 'back'
variable3 = data[variable3]

# An . . . .. a day keeps the doctor away!
column3 = "apple"

# load header from file
for idx,elem in enumerate(header1):
    # if answer of last question is in the header, then query the data
    if elem==column3:
        break
else:
    print column1+" not found in header of the file - check the last question"
    exit

# calculate mean value of the third column of the first downloaded file
row3 = clue1_array[:,idx].mean()

# load value from variabl3 with the specific row information
filename4 = variable3[row3]

# if value can taken as integer, then it will be changed to integer
if filename4==int(filename4):
    filename4 = int(filename4)

# download the binary file
url = download_page+str(filename4)+".bin"
print "Downloading: " + url

f = urllib2.urlopen (url)
with open(os.path.basename(url), "wb") as local_file:
          local_file.write(f.read())

file = open("101010.bin", 'rb')
template = file.read(107)
print template

exec "dt = np."+template
#dt = np.dtype([('sunburnedpenguin', '<i2'), ('newspaper', '<i2'), ('redzebra', '<i2'), ('embarresedskunk', '<i2')])

file4 = np.fromfile("101010.bin", dtype=dt)
print file4


#SAMPLE CODE FROM WEB FOR WRITING HDF5 files
#clue5

# Alive without breath, as cold as death; never thirsty, ever drinking, all in mail, never
# clinking.
column5 = "fish"

# What gets wetter and wetter the more it dries?
variable5a = "towel"

# What is black and white and red all over?
variable5b ="sunburnedpenguin"

"""
# write netcdffile
file = NetCDFFile('rectilinear.nc', 'w')
write_rectilinear(file, nodal, 'data', x_coord, y_coord)
file.close()
"""


# ---------------------------   in progress ----------------
f = h5py.File('myfile.hdf5','w')

# longitude
dset = f.create_dataset("longitude", data=arr)

# latitude
dset = f.create_dataset("latitude", data=arr)

# dataset
g = np.array(file4)
dset = f.create_dataset("dataset", data=file4)

g = np.asmatrix(file4)

#[(29796, 28793, 10341, 10331), (29479, 28277, 30050, 28274),25701


longitude = 0

 # Create a new file using the default properties.
fid = h5py.h5f.create(FILE)

# Create the dataspace.  No maximum size parameter needed.
dims = (DIM0, DIM1)
space_id = h5py.h5s.create_simple(dims)

# Create the dataset creation property list.  Set the layout to compact.
dcpl = h5py.h5p.create(h5py.h5p.DATASET_CREATE)
dcpl.set_layout(h5py.h5d.COMPACT)

# Create the datasets using the dataset creation property list.
dset = h5py.h5d.create(fid, DATASET, h5py.h5t.STD_I32BE, space_id, dcpl)

# Write the data to the dataset.
dset.write(h5py.h5s.ALL, h5py.h5s.ALL, wdata)



