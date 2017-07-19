import sys,csv
from travis_user import travis_user
from github_module import extract_code
def get_error_snippet(error, text):
    error_index =  text.index(error)
    return text[error_index-450:error_index+400]
    
handle = open("key.txt","r")
key = handle.readline()
handle.close()
me = travis_user(key)
f = open("travistorrent_8_2_2017.csv","r+")
error_type = open('error_list.txt', 'r').read()
handle = open("repo_java_maven.txt","r+")
csv.field_size_limit(sys.maxint)
reader = csv.reader(f)
ruby =0
java_marven=0
java_ant=0
java_gradle=0
python = 0
plain =0
lan = "ruby"
des = [0]
for row in reader:
    try:
        
        if row[1] not in des:
            des.append(row[1])
            #lan = me.getlanguage(row[1])
            if row[1].find("rackerlabs/blueflood")==0:
                print row[0]
            continue
            #print lan
        else:
            continue
    except:
        pass
    if lan.find("plain")==0:
        try:
            #lan = me.getlanguage(row[1])
            pass
        except:
            pass
        plain = plain +1
    if lan.find("ruby")==0:
        ruby = ruby + 1
    else:
        if (lan.find('java')==0) and (row[61].find("FALSE") == 0):
            print "got one"
            
            try:            
                java_ant = java_ant + 1
                handle.write(row[1])
                build_id = int(row[0])
                build = me.user.build(build_id)
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
                        else:
                            if lan.find('java-maven')==0:
                                java_marven = java_marven + 1
                            else:
                                 if lan.find('java-gradle')==0:
                                     java_gradle = java_gradle + 1
                                 else:
                                     if lan.find('python')==0:
                                         python = python + 1
                                     else:
                                         #print lan+ "  " + row[1]
                                         pass
             
            except:
                  pass
print ruby
print java_ant
print java_marven
print java_gradle
print python
print plain
f.close()