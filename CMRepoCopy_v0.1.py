
#!/usr/bin/env python

import sys
import os

def main():
        #method 1: AWS EC2 instance
        ec2way()
def ec2way():
        pemfile=raw_input('please enter the path of your pem file: ')
        #Update the URL 
        cmpath=("sudo wget http://archive.cloudera.com/cm5/redhat/6/x86_64/cm/cloudera-manager.repo")
        if len(pemfile)!=0 and os.path.isfile(pemfile) and pemfile.endswith('.pem'):
                loginuser=raw_input('Enter the login user (ex: "ec2-user") : ')
                hostips=raw_input('Enter the public ips of your instances except for current host seperated by "," :')

                for eachhost in hostips.split(','):
                        print eachhost
                        print 'Cm path is '+cmpath
                        checkrepo="if test -f '/etc/yum.repos.d/cloudera-manager.repo'; then echo 'Updating CM repo';sudo rm /etc/yum.repos.d/cloudera-manager.repo;cd /etc/yum.repos.d;"+cmpath+";else echo 'adding CMrepo' ;cd /etc/yum.repos.d;"+cmpath+";fi"
                        sshtohost= 'ssh -i '+pemfile+' -t '+loginuser+'@'+eachhost+' " '+checkrepo+'"'
                        os.system(sshtohost)
                        #print sshtohost
if __name__ == "__main__":
    main()                                              
