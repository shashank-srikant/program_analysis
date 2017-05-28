# -*- coding: utf-8 -*-
"""
Created on Fri May 26 03:24:38 2017

@author: uka_in
"""
from travispy import TravisPy
import os

class travis_user(object):
    user = ''
    category=''
    job_id=''
    build_id = ''
    travis_lang=''
    repo_slug=''
    job=''
    commit_id=''
    
    def __init__(self,key):
        self.user = TravisPy.github_auth( key )
    
    def getlog(self,job_id):
        log_content=self.job.log.body
        log_content = log_content.encode('utf-8')
        return log_content
    
    def getinfo(self,job_id):
        self.job_id=job_id
        self.job = self.user.job(self.job_id)
        self.commit_id = self.job.commit_id
        self.repo_slug=self.user.repo(self.job.repository_id).slug
        self.build_id=self.job.build_id
        travis_info=self.user.build(self.build_id).config
        self.travis_lang=travis_info['language']
        return [self.repo_slug,self.build_id,travis_info,self.travis_lang]

    def write_log(self):
        fh2=open("log.txt","w+")
        fh2.write(self.getlog(self.job_id))
        fh2.close()
        
    def write_info(self):
        fh2=open("info.txt","w+")
        fh2.write(str(self.travis_lang)+','+str(self.repo_slug)+','+str(self.commit_id))
        fh2.close()



handle = open("key.txt","r")
key = handle.readline()
handle.close()
me = travis_user(key)

with open("result.txt","r")as fh:
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