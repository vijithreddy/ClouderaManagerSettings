#!/usr/bin/env python

import sys
import os
import getpass

def main():
        #This snippet can be done host by host or uncomment section 2 for installing repo from one host
        wgetreposfile=('wget -O cmrepofile.py http://ge.tt/api/1/files/1sBjd3J2/0/blob?download')
        os.system(wgetreposfile)
        change='sudo chmod 755 cmrepofile.py'
        os.system(change)
    	#Cm repo addition
        os.chdir('/etc/yum.repos.d')
        if os.path.isfile('cloudera-manager.repo'):
                removecm=('sudo rm cloudera-manager.repo')
                os.system(removecm)
        wgetcm=('sudo wget http://archive.cloudera.com/cm5/redhat/6/x86_64/cm/cloudera-manager.repo')
        os.system(wgetcm)
        os.chdir('/home/'+getpass.getuser())
        print os.getcwd()
        ##########################################
        # Section 2: This section is for copying the file to remote instances
        #method 1: AWS EC2 instance
        ec2way()


def ec2way():
        pemfile=raw_input('please enter the path of your pem file: ')
        if len(pemfile)!=0 and os.path.isfile(pemfile) and pemfile.endswith('.pem'):
                hostips=raw_input('Enter the public ips of your instances except for current host seperated by "," :')
                for eachhost in hostips.split(','):
                        print eachhost
                        copyrepo=('scp -i '+pemfile+' ~/cmrepofile.py /etc/yum.repos.d/cloudera-manager.repo ec2-user@'+eachhost+':.')
                        os.system(copyrepo)
                        sshtohost=('ssh -i '+pemfile+' -t ec2-user@'+eachhost+' "python cmrepofile.py"')
                        os.system(sshtohost)

if __name__ == "__main__":
    main()
