import sys,csv
from travis_user import travis_user
handle = open("key.txt","r")
key = handle.readline()
handle.close()
me = travis_user(key)
f = open("travistorrent_8_2_2017.csv","rb")
csv.field_size_limit(sys.maxint)
reader = csv.reader(f)
ruby =0
java_marven=0
java_ant=0
java_gradle=0
python = 0

for row in reader:
    lan = str(row[50])
    if lan.find("plain")==0:
        lan = me.getlanguage(row[1])
    if lan.find("ruby")==0:
        ruby = ruby + 1
    else:
        if lan.find('java-ant')==0:
            java_ant = java_ant + 1
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
                         print lan+ "  " + row[1] 

print ruby
print java_ant
print java_marven
print java_gradle
print python

f.close()