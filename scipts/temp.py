# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 18:04:34 2017

@author: root
"""
import requests,json
from travis_user import travis_user
import github_module

def get_error_snippet(error, text):
    error_index =  text.index(error)
    return text[error_index-450:error_index+400]
    
def RetNextBuildId(repo_slug,build_id):
    url = ' https://api.travis-ci.org/repos/' + repo_slug+'/builds/'+str(build_id)
    url2 = ''
    my_headers = { 'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.5) Gecko/2009011615 Firefox/3.0.5 CometBird/3.0.5','Accept': 'application/vnd.travis-ci.2+json'
    ,'Host': 'api.travis-ci.org' }
    payload = {}
    try:
        r = requests.get( url, params = payload, headers = my_headers)
    except:
        print('Network/site unreachable!!')
        return 0
    try:
        response = json.loads(r.text)
        build_number = response['build']['number']
        print build_number
        url2 = ' https://api.travis-ci.org/repos/' + repo_slug+'/builds?number='+str(int(build_number)+1)
        #return last_build_number
    except:
        print('Invalid JSON!!')
        return 0
    try:
        r2 = requests.get( url2, params = payload, headers = my_headers)
    except:
        print('Network/site unreachable!!')
        return 0
       
    try:
        response = json.loads(r2.text)
        print response
        build_id2 = response['builds'][0]['id']
        return build_id2
    except Exception,e:
        print('Invalid JSON!!')
        print e.args
        return 0
    
def ret_commit_sha(me,build_id):
    build = me.user.build(build_id)
    commit = build.commit
    commit_sha = commit.sha
    return commit_sha
    
handle = open("key.txt","r")
key = handle.readline()
handle.close()
me = travis_user(key)
error_type = open('error_list.txt', 'r').read()
build_id = "120405"
repo_slug = me.user.build(build_id).repository.slug
print repo_slug
build_state="failed"
build_id2=build_id
while build_state.find("failed")==0 or build_state.find("errored")==0:
    
    build_id2=RetNextBuildId(repo_slug,build_id2)
    build_state = me.user.build(build_id2).state

print build_state,build_id2
commit_sha1 = ret_commit_sha(me,build_id)
commit_sha2 = ret_commit_sha(me,build_id2)
patch = github_module.comp_commit(repo_slug,commit_sha1,commit_sha2)
print patch
if build_id2 != 0:
    build = me.user.build(build_id2)
    commit = build.commit
    commit_sha = commit.sha
    jobs = build.jobs
    for job in jobs:
        log = job.log
        log_body = log.body
        for error in error_type.split(','):
            if (str(error) in log_body) and error!=' ' and error!='\n':
                print "got one error"
                error_snippet = get_error_snippet(error, log_body)
                file_h = open(str(job.log_id)+".txt", "w")
                file_h.write(error_snippet)
                #file_h.write(str(extract_code(me.repo_slug, commit_sha)))
                file_h.close()
                print("Log written")
    #return last_build_number
else:
    print "Error Encountered!!!!"

    