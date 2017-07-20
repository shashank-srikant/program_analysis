# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 17:27:19 2017

@author: root
"""

import sys,csv
from travis_user import travis_user
handle = open("key.txt","r")
key = handle.readline()
handle.close()
me = travis_user(key)
f = open("travistorrent_8_2_2017.csv","rb")
handle = open("builds.txt","r+")
csv.field_size_limit(sys.maxint)
reader = csv.reader(f)
build_no = [0]

for row in reader:
    slug = row[1]
    if slug.find("geoserver/geoserver")==0:
        #print build_no
        if row[0] not in build_no:
            build_no.append(row[0])
            handle.write(row[0] + "   " + str(row[61]))
            handle.write("\n")

handle.close()
f.close()