#!/usr/bin/env python

import sys
import os

def main():
	#This snippet can be done host by host or uncomment section 2 for installing repo from one host
	os.chdir('/etc/yum.repos.d')
	removecm=('sudo rm cloudera-manager.repo')
	os.system(removecm)
	wgetcm=('sudo wget http://archive.cloudera.com/cm5/redhat/6/x86_64/cm/cloudera-manager.repo')
	os.system(wgetcm)
	exitsytem('exit')
	os.system(exitsytem)
	##########################################

if __name__ == "__main__":
    main()
