# -*- coding: utf-8 -*-
import os
from travis_user import travis_user


handle = open("key.txt","r")
key = handle.readline()
handle.close()
me = travis_user(key)

with open("result_1.txt","r")as fh:
    os.chdir('logs/')
    for line in fh:
        if line[0] != '#':
                job_id=(int)(line.split('/')[5])
                me.getinfo(job_id)
                os.mkdir(str(me.job_id))
                os.chdir(str(me.job_id))
                me.write_log()
                me.write_info()
                print me.repo_slug
                print me.commit_sha
                print os.getcwd()
                os.chdir('../')
                
        else:
            if os.getcwd() != "/var/www/html/program_analysis/scipts/logs":
                os.chdir('../')
            else:
                category=line.replace('#','')
                try:            
                    os.mkdir(category)
                    os.chdir(category)
                except:
                    os.chdir(category)  
                
                print os.getcwd()
                
fh.close()                