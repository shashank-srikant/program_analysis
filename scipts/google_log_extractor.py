#after 2-3 times of usage google might block this script, in that case change https to http in url also try changing user-agent
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 03:02:17 2017

@author: uka_in
"""

import requests, re
from bs4 import BeautifulSoup
 
def error_list(filename):
    try:
        fh2=open(filename,"r")
    except:
        print("Cannot open file!! Aborting!!")
        exit(0)
    for line in fh2:
        if line[0]!='#':
            error=line[0:len(line)].split(',');
            
    error=error[0:7]
    fh2.close()
    return error

def google_scrap(filename,error_list,url,headers,number_of_queries):
    try:
        fh=open(filename,'w+')
    except:
        print("Cannot open file with write permission!! Aborting!!")
        exit(0)
        
    for handle1 in error_list:
        fh.write('#'+handle1+'\n')
        for handle2 in number_of_queries:
            payload = { 'q' : 'intext:'+ handle1 +' site:https://s3.amazonaws.com/archive.travis-ci.org/jobs/', 'start' : str(handle2) }
            r = requests.get( url, params = payload, headers = headers)
            
            soup = BeautifulSoup( r.text, 'html.parser' )
             
            h3tags = soup.find_all( 'h3', class_='r' )
             
            for h3 in h3tags:
                try:
                    #print(re.search('url\?q=(.+?)\&sa', h3.a['href']).group(1))
                    fh.write( re.search('url\?q=(.+?)\&sa', h3.a['href']).group(1)+'\n' )
                except:
                    continue
    fh.close()

url = 'https://www.google.com/search'
my_headers = { 'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.5) Gecko/2009011615 Firefox/3.0.5 CometBird/3.0.5' }
number_of_queries = [0,10];
error=error_list("error_list.txt")
google_scrap("result_1.txt",error,url,my_headers,[0,10])