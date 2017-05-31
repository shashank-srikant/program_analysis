from travis_user import travis_user

handle = open("key.txt","r")
key = handle.readline()
handle.close()
me = travis_user(key)
url=raw_input("Enter github repository url");
if me.init_repo(url):
    builds = me.get_build()
    print builds