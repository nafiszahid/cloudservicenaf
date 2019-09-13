#!/usr/bin/python
import time,commands

commands.getoutput('sudo yum install nfs-utils rpcbind -y')
commands.getoutput('sudo mkdir /media/Qw')
commands.getoutput('sudo mount -t nfs 192.168.1.100:/mnt/Qw /media/Qw')
commands.getoutput('sudo iptables -F')
commands.getoutput('sudo setenforce 0')
commands.getoutput('sudo systemctl start rpcbind')