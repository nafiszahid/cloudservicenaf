#!/usr/bin/python2
import cgi
import os
import commands
import time

print "content-type:text/html"
print ""

data=cgi.FieldStorage()
dirname=data.getvalue('dname')
dirsize=data.getvalue('dsize')
password=data.getvalue('passwd')

commands.getoutput("sudo yum install samba -y")
vg="myhd"
commands.getoutput("sudo lvcreate --name "+dirname+" --size "+dirsize+"M "+vg)
commands.getoutput("sudo mkfs.ext4 /dev/"+vg+"/"+dirname)
commands.getoutput("sudo mkdir /mnt/"+dirname)
commands.getoutput("sudo mount /dev/mapper/"+vg+"-"+dirname + " /mnt/"+dirname)
msg="\n["+dirname+"]\npath=/mnt/"+dirname+"\nwritable=yes\n"

f=open("/etc/samba/smb.conf",'a+')
f.write(msg)
f.close()

commands.getoutput("sudo useradd -s /sbin/nologin "+dirname)
commands.getoutput("(echo "+password+";echo "+password+")| sudo smbpasswd -a -s "+dirname)

commands.getoutput("sudo systemctl restart smb")
commands.getoutput("sudo iptables -F")
commands.getoutput("sudo setenforce 0")

web='''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>STAAS CLOUD</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/static/template1.css">
  <script src="/static/template2.js"></script>
  <script src="/static/template3.js"></script>
</head>
<body style="background-color:powderblue">
<div class="container">
  <h1 style="color:red">STAAS CLOUD</h1>
  <div class="list-group">
    <h3>Follow the instructions listed:</h3>
    <p>Open <b>RUN</b></p>
    <p>Type -> <b>\\server_ip\drive_name</b></p>
    <p>Click on <b>OK</b></p>
    <p>Enter <b>username</b> and <b>password</b><p>
  </div>
</div>

</body>
</html>
'''

print web
