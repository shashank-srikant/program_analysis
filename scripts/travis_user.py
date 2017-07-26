from travispy import TravisPy

#This class initializes the user and provides function for some specific task
#   Variables:
#           user - stores user object returned by travis API after authentication
#           category - stores the type of error present in the log, this variable might remain uninitialized
#           job_id - stores job_id belonging to the log
#           build_id - stores build_id corresponding to a commit
#           travis_lang - stores programming language as mentioned in .travis.yml
#           repo_slug - stores repository slug ,example: madaari/Test-code-base
#           job - stores job object as specified in travis API
#           commit_id/sha - stores commit id/sha
#           repo - stores repository object as specified in travis API

class travis_user(object):
    user = ''
    category=''
    job_id=''
    build_id = ''
    travis_lang=''
    repo_slug=''
    job=''
    commit_id=''
    commit_sha=''
    repo=''
    
#This function authenticates the user using github OAuth token
#NOTE: OAuth token should have following permissions:-  read:org, repo:status, repo_deployment, user:email, write:repo_hook
#Input: authentication token, string
#Output: NONE
#Example:
#
#   I/P: travis_user( "<Github token>" )
#
#   O/P: NONE
#       
#  
    
    def __init__(self,key):
        self.user = TravisPy.github_auth( key )

#This function initializes all necessary variables depending on a given github repository url
#Input: repo_url: github repository url
#Note: Remove backslash after repository name
#Output: 1
#Example:
#
#   I/P: self.init_repo("https://github.com/madaari/Test-code-base")
#
#   O/P: 1
#       
#  

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

#This function extracts the log corresponding to a job_id
#Input: NONE
#Output: string, log content
#Example:
#
#   I/P: getlog()
#
#   O/P: <content>
#       
#  
 
    def getlog(self):
        log_content=self.job.log.body
        log_content = log_content.encode('utf-8')
        return log_content

    def getlanguage(self,slug):
        repo = self.user.repo(slug)
        last_build = repo.last_build
        config = last_build.config
        return config['language']
#This function extracts all important information corresponding to job_id
#Input: job_id, string
#Output: Array of all important information
#Example:
#
#   I/P: getinfo(<job_id>)
#
#   O/P: 
#       
#  

    def getinfo(self,job_id):
        self.job_id=job_id
        self.job = self.user.job(self.job_id)
        self.commit_id = self.job.commit_id
        self.repo_slug=self.user.repo(self.job.repository_id).slug
        self.build_id=self.job.build_id
        build = self.user.build(self.build_id)
        commit = build.commit
        self.commit_sha = commit.sha
        travis_info=self.user.build(self.build_id).config
        self.travis_lang=travis_info['language']
        return [self.repo_slug,self.build_id,travis_info,self.travis_lang]

#This function gets all build ids corresponding to a repository
#Input: NONE
#Output: array of build object
#Example:
#
#   I/P: get_build()
#
#   O/P: 
#       [<travispy.entities.build.Build object at 0x7fb49a818758>, ...]
#   
  
    def get_build(self):
        if self.repo.active != 1:
            print("Repository not active, please enter another url")
            return 0
        else:
           builds = self.user.builds(slug=self.repo_slug)
           return builds

#This function will write the log to a text file named log.txt
#Input: NONE
#Output: NONE
#Example:
#
#   I/P: write_log()
#
#   O/P: NONE
#       
#           
   
    def write_log(self):
        try:
            fh2=open("log.txt","w+")
        except:
            print('Could not open the file in write mode. Aborting!!')
            exit(0)
        fh2.write(self.getlog())
        fh2.close()

#This function will write all information to a text file named info.txt
#Input: NONE
#Output: NONE
#Example:
#
#   I/P: write_info()
#
#   O/P: NONE
#       
#       
          
    def write_info(self):
        try:
            fh2=open("info.txt","w+")
        except:
            print('Could not open the file in write mode. Aborting!!')
            exit(0)
        fh2.write(str(self.travis_lang)+','+str(self.repo_slug)+','+str(self.commit_id))
        fh2.close()
    
       

