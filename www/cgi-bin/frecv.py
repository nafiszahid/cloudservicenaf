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

commands.getoutput("sudo yum install nfs-utils rpcbind -y")
commands.getoutput("sudo systemctl start nfs-server")
commands.getoutput("sudo systemctl start rpcbind")
commands.getoutput("sudo fallocate -l " + dirsize + "M " + "/tmp/"+dirname)
commands.getoutput("sudo mkfs.xfs /tmp/"+dirname)

commands.getoutput("sudo mkdir /mnt/"+dirname)
commands.getoutput("sudo mount /tmp/"+dirname + " /mnt/" + dirname)
msg="sudo /mnt/" + dirname + " 192.168.1.100(rw,no_root_squash)"

f=open("/etc/exports",'a+')
f.write(msg)
f.close()

commands.getoutput("sudo systemctl restart nfs-server")
commands.getoutput("sudo systemctl enable nfs-server")
commands.getoutput("sudo exportfs -r")
commands.getoutput("sudo iptables -F")
commands.getoutput("sudo setenforce 0")
msg = "#!/usr/bin/python\nimport time,commands\n\ncommands.getoutput('sudo yum install nfs-utils rpcbind -y')\ncommands.getoutput('sudo mkdir /media/" + dirname + "')\ncommands.getoutput('sudo mount -t nfs 192.168.1.100:/mnt/"+ dirname + " /media/" + dirname +"')\ncommands.getoutput('sudo iptables -F')\ncommands.getoutput('sudo setenforce 0')\ncommands.getoutput('sudo systemctl start rpcbind')"

f = open("/var/www/html/fclient.sh","w")
f.write(msg)
f.close()

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
    <a href="/fclient.sh" class="list-group-item"><b>Download the file and get your storage</b></a>
    <b>NOTE: AFTER DOWNLOADING THE FILE GIVE IT THE EXECUTION POWER</b>
  </div>
</div>

</body>
</html>
'''

print web
