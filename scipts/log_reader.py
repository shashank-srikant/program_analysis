# -*- coding: utf-8 -*-
"""
Created on Fri May 26 03:24:38 2017

@author: uka_in
"""
from travispy import TravisPy
user = TravisPy.github_auth( '9ed26325b1c47ef8fad50a7928984d05fc51adb3' )
category=''
with open("result.txt","r")as fh:
    for line in fh:
        if line[0] != '#':
                job_id=(int)(line.split('/')[5])
                job=user.job(job_id)
                repo=user.repo(job.repository_id)
                print(str(repo.slug)+' '+str(repo.github_language)+' '+str(job.build_id) )
                log_content=job.log.body
                print(log_content.find(category))
        else:
            category=line.replace('#','')
                
fh.close()