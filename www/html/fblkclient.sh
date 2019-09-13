#!/usr/bin/python

import time,commands

commands.getoutput('sudo yum install iscsi-initiator-utils -y')
q=commands.getoutput('sudo iscsiadm --mode discoverydb --type sendtargets --portal 192.168.1.100 --discover')
p=q.split()[1]
commands.getoutput('iscsiadm --mode node --targetname '+p+' --portal 192.168.1.100:3260 --login')
commands.getoutput('sudo iptables -F')
commands.getoutput('sudo setenforce 0')

