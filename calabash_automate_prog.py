import os
import time
import sh
import re
import sys
from slackclient import SlackClient


# token = "xoxp-13033156818-13029296503-30705606503-4867886422"
# sc = SlackClient(token)


#The installation of sh is done through the pip command
#$> pip install sh
# pip install slackclient

# sends terminal output to text file named "output.txt"
# python testpythonstuff.py > output.txt

#os.system("cd ~/workspace/xhome-android-qa/ANDROID-TESTS/xhome_android_automation")
#os.system("calabash-android run xfinityhome-tps-release-7.10.6.255117.apk features/sanity_tests.feature")

#sh.run("calabash-android run xfinityhome-tps-release-7.10.6.255117.apk features/sanity_tests.feature")
#os.system("pwd | ls")

# how to run in terminal: python testpythonstuff.py > calabashresults.txt

# changes directory, runs ruby cleanup and git pull, then resigns the apk before running calbash tests. After calabash tests finish, directory is changed where "readfile_python.py" is located and runs it.
while True:
    sh.cd("/Users/darmst001c/workspace/xhome-android-qa/ANDROID-TESTS/xhome_android_automation")
    print(sh.pwd())
    os.system("ls")
    os.system("ruby cleanup.rb")
    time.sleep(5)
    os.system("git pull")
    time.sleep(10)
    os.system("bundle exec calabash-android resign xfinityhome-tps-release-7.14.0.262621.apk")
    os.system("bundle exec calabash-android run xfinityhome-tps-release-7.14.0.262621.apk features/smoke_tests.feature")
    time.sleep(5)
    sh.cd("/Users/darmst001c/python")
    os.system("python readfile_python.py")

"""
    # opens calabashresults.txt and use regex to find match of scenario and steps, then prints matches to terminal
    textfile = open("calabashresults.txt", "r")

    for line in textfile:
        if re.match("(.*)scenario(.*)", line):
            print line
        if re.match("(.*)steps(.*)", line):
            print line

    with open("calabashresults.txt") as f:
        last = None
        for line in (line for line in f if line.rstrip('\n')):
            last = line
    print last
"""



    #slack.chat.post_message('#testing2', print line, last)

#slack.files.upload('/Users/darmst001c/python/output.txt')
#slack.files.upload('#testing2', '/Users/darmst001c/python/output.txt')
#slack.chat.post_message('#testing2', 'Hellow fellow slackers!')
#slack.files.upload("#testing", "output.txt")
