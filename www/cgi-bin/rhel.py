#!/usr/bin/python2
import cgi
import os
import commands
import time

print "content-type:text/html"
print ""
data=cgi.FieldStorage()
dirname=data.getvalue('dname')
dirram=data.getvalue('dram')
dircpu=data.getvalue('dcpu')

print os.system('sudo qrencode -s 8*8 -o /var/www/html/images/wow.png http://192.168.1.100:6080')
print os.system('sudo virt-install --cdrom /root/Downloads/rhel-server-7.2-x86_64-dvd.iso --ram '+dirram+' --vcpu '+dircpu+' --nodisk --name '+dirname+' --graphics vnc,port=5950,listen=0.0.0.0 &')
print os.system('sudo websockify --web=/usr/share/novnc 6080 0.0.0.0:5950 &')

web='''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>IAAS CLOUD</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/static/template1.css">
  <script src="/static/template2.js"></script>
  <script src="/static/template3.js"></script>
</head>
<body style="background-color:powderblue">
<div class="container">
  <h1 style="color:red">IAAS CLOUD</h1>
  <div class="list-group">
    <a href='http://192.168.1.100:6080'>Here is your OS</a><br><br>
    <a href='/images/wow.png'>You can also use the OS on phone by scanning the generated QR code</a>
  </div>
</div>

</body>
</html>
'''

print web
