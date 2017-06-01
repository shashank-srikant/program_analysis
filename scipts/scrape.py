from travis_user import travis_user

handle = open("key.txt","r")
key = handle.readline()
handle.close()
me = travis_user(key)
url=raw_input("Enter github repository url");
if me.init_repo(url):
    builds = me.get_build()
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
            