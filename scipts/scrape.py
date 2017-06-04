from travis_user import travis_user
import os

def get_error_snippet(error, text):
    error_index =  text.index(error)
    return text[error_index-150:error_index+100]
    
handle = open("key.txt","r")
key = handle.readline()
handle.close()
me = travis_user(key)
url=raw_input("Enter github repository url")
error_type = open('error_list.txt', 'r').read()
if me.init_repo(url):
    builds = me.get_build()
    print("build retrieved")
    os.chdir(os.getcwd()+'/logs/')
    for build in builds:
        if build.state == 'failed':
            custom_build = me.user.build(build.id)
            failed_jobs = custom_build.job_ids
            for job_id in failed_jobs:
                job = me.user.job(int(job_id))
                log = job.log.body
                log = log.encode('utf-8')
                for error in error_type.split(','):
                    if (str(error) in log) and error!=' ' and error!='\n':
                        error_snippet = get_error_snippet(error, log)
                        file_h = open(str(job_id)+".txt", "w")
                        file_h.write(error_snippet)
                        file_h.close()
                        print("Log written")   
                
        else:
            print("Build passed!! no error")
    
#    for content in os.listdir(os.getcwd()):
#                try:
#                    text = open(content,'r').read()
#                except:
#                    print('cannot open file, skipping!!')
#                file_h = open(me.repo_slug.split('/')[0]+".txt", "w+")
#                for error in error_type.split(','):
#                    if (str(error) in text) and error!=' ' and error!='\n':
#                        error_snippet = get_error_snippet(error, text)
#                        print('-------------------------------------------')
#                        file_h.write(error_snippet)
#                fh.close()
#                file_h.close()