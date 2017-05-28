# -*- coding: utf-8 -*-
"""
Created on Sun May 28 19:39:15 2017

@author: root
"""
from travispy import TravisPy

class travis_user(object):
    user = ''
    job_id=''
    build_id = ''
    travis_lang=''
    repo_slug=''
    job=''
    commit_id=''
    repo=''
    
    def __init__(self,key):
        self.user = TravisPy.github_auth( key )
        
    def init_repo(self, repo_url):
        temp = repo_url.split('/')
        repo_slug = temp[len(temp)-2]+'/'+temp[len(temp)-1]
        self.repo_slug = repo_slug
        try:
            self.repo = self.user.repo(self.repo_slug)
        except:
            print("Repo not associated with travis or url is wrong!!")
            return 0
        return 1
       
    def get_build(self):
        if self.repo.active != 1:
            print("Repository not active, please enter another url")
            return 0
        else:
           builds = self.user.builds(slug=self.repo_slug)
           return builds
        
handle = open("key.txt","r")
key = handle.readline()
handle.close()
me = travis_user(key)
url=raw_input("ENter github repository url");
if me.init_repo(url):
    builds = me.get_build()
    print builds