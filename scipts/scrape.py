from travis_user import travis_user
import os

def get_error_snippet(error, text):
    error_index =  text.index(error)
    return text[error_index-150:error_index+100]
    
handle = open("key.txt","r")
key = handle.readline()
handle.close()
me = travis_user(key)
url=raw_input("Enter github repository url");
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
                fh = open(str(job.log_id)+".txt","w+")
                fh.write(log)
                fh.close
                print("Log written")
            for content in os.listdir(os.getcwd()):
                try:
                    text = open(content,'r').read()
                except:
                    print('cannot open file, skipping!!')
                error_type = open('error_list.txt', 'r').read()
                for error in error_type.split(','):
                    if (str(error) in text) and error!=' ' and error!='\n':
                        print get_error_snippet(error, text)
                        print('-------------------------------------------')
                fh.close()
        else:
            print("Build passed!! no error")