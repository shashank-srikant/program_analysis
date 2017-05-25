#after 2-3 times of usage google might block this script, in that case change https to http in url also try changing user-agent
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 03:02:17 2017

@author: uka_in
"""

import requests, re
from bs4 import BeautifulSoup
 
fh=open("result.txt",'w+')
url = 'https://www.google.com/search'
my_headers = { 'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.5) Gecko/2009011615 Firefox/3.0.5 CometBird/3.0.5' }
start = [0,10];
error = ['SyntaxError:','ZeroDivisionError:','NameError:','EOFError:','AssertionError:','IndentationError:','ValueError:']
for handle1 in error:
    fh.write('#'+handle1+'\n')
    for handle2 in start:
        payload = { 'q' : 'intext:'+ handle1 +' site:https://s3.amazonaws.com/archive.travis-ci.org/jobs/', 'start' : str(handle2) }
        r = requests.get( url, params = payload, headers = my_headers)
        
        soup = BeautifulSoup( r.text, 'html.parser' )
         
        h3tags = soup.find_all( 'h3', class_='r' )
         
        for h3 in h3tags:
            try:
                #print(re.search('url\?q=(.+?)\&sa', h3.a['href']).group(1))
                fh.write( re.search('url\?q=(.+?)\&sa', h3.a['href']).group(1)+'\n' )
            except:
                continue
 
fh.close()
