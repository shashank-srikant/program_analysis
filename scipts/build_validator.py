# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 18:25:15 2017

@author: root
"""
from travis_user import travis_user
handle = open("key.txt","r")
key = handle.readline()
handle.close()
me = travis_user(key)
f = open("builds.txt","rb")
for line in f:
    #print int(line)
    build = me.user.build(int(line))
    repo = build.repository
    print repo.slug