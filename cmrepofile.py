#!/usr/bin/env python

import sys
import os

def main():
	os.chdir('/etc/yum.repos.d')
        if os.path.isfile('cloudera-manager.repo'):
                removecm=('sudo rm cloudera-manager.repo')
                os.system(removecm)
        wgetcm=('sudo wget http://archive.cloudera.com/cm5/redhat/6/x86_64/cm/cloudera-manager.repo')
        os.system(wgetcm)

if __name__ == "__main__":
    main()
