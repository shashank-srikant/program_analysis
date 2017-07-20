import sys,csv,os
from travis_user import travis_user
import requests,json
from github_module import extract_code
def get_error_snippet(error, text):
    error_index =  text.index(error)
    return text[error_index-450:error_index+400]
    
def extract_error_build(repo_slug):
    pass
    last_build_no = extract_last_build_number(repo_slug)
    print last_build_no

def extract_last_build_number(repo_slug):
    url = ' https://api.travis-ci.org/repos/' + repo_slug+'/builds'
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
        last_build_number = response['builds'][0]['number']
        return last_build_number
    except:
        print('Invalid JSON!!')
        return 0
    
handle = open("key.txt","r")
key = handle.readline()
handle.close()
me = travis_user(key)
f = open("travistorrent_8_2_2017.csv","r+")
error_type = open('error_list.txt', 'r').read()
#handle = open("repo_java_maven.txt","r+")
csv.field_size_limit(sys.maxint)
reader = csv.reader(f)
des = [0]
os.chdir(os.getcwd()+'/logs/')
for row in reader:
    try:
        
        if row[1] not in des:
            repo_slug = row[1]
            #repo_slug = repo_slug.replace('/','-')
            des.append(repo_slug)
            repo = me.user.repos( slug=repo_slug )
            print repo[0].last_build_number
            continue
            #lan = me.getlanguage(row[1])
            print os.getcwd()+'/'+repo_slug
            os.mkdir(repo_slug)
            print os.listdir(os.getcwd())
            os.chdir(repo_slug)
            extract_error_build(repo_slug)
            os.chdir("../")
            continue
            #print lan
        else:
            continue
    except Exception,e:
        print e.args
        print("Error encountered" + row[1])
        pass
    
   