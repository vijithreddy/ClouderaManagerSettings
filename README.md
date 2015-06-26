This repo contains three files:
CMRepoCopy_v0.1, cmrepos.py and cmrepofile.py

CMRepoCopy_v0.1:

This is the most updated script, it can copy CM repo to a single host or to multiple hosts. The advantage this script has over the other two is that it can be executed on any remote machine which can access the host machines.

Future updates will be done to this script to accommodate in premesis clusters (currently only done through aws ec2).


cmrepo.py:

This file is used if you want clouderamanger repo stored in various ec2 instances.
Future updates will be done for simple ssh between systems in a cluster.

cmrepofile.py:

This file is to install CM repo for only single instance.
