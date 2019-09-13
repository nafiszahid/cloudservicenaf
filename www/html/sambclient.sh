#!/usr/bin/python
import time,commands

commands.getoutput('yum install cifs-utils samba-client -y')
commands.getoutput('mkdir /media/1')
commands.getoutput('mount -t cifs -o username=1  //192.168.1.100/1 /media/1')
commands.getoutput('iptables -F')
commands.getoutput('setenforce 0')