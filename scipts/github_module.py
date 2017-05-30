# -*- coding: utf-8 -*-
import requests, json

def comp_commit(repo_slug,com1, com2):
    url = 'https://api.github.com/repos/' + repo_slug + '/compare/' + com1 + '...' + com2
    my_headers = { 'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.5) Gecko/2009011615 Firefox/3.0.5 CometBird/3.0.5' }
    payload = {}
    try:
        r = requests.get( url, params = payload, headers = my_headers)
    except:
        print('Network/site unreachable!!')
        return 0
    try:
        response = json.loads(r.text)
    except:
        print('Invalid JSON!!')
        return 0
    patch = response['files'][0]['patch']
    return patch
    
def extract_code(repo_slug,com1):
    url = 'https://api.github.com/repos/'+repo_slug+'/commits/'+com1
    my_headers = { 'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.5) Gecko/2009011615 Firefox/3.0.5 CometBird/3.0.5' }
    payload = {}
    result=[]
    try:
        r = requests.get( url, params = payload, headers = my_headers)
    except:
        print('Network/site unreachable!!')
        return 0
    try:
        response = json.loads(r.text)
    except:
        print('Invalid JSON!!')
        return 0
    for file in response['files']:
        url = file['raw_url']
        result.append(url)
        print url
    return result
        
print comp_commit('madaari/Test-code-base','d2f86af2825f','8e821bea30ad')
print extract_code('madaari/Test-code-base','8e821bea30ad')