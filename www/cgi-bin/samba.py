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
msg = "#!/usr/bin/python\nimport time,commands\n\ncommands.getoutput('yum install cifs-utils samba-client -y')\ncommands.getoutput('mkdir /media/" + dirname + "')\ncommands.getoutput('mount -t cifs -o username="+dirname+"  //192.168.1.100/"+ dirname + " /media/" + dirname +"')\ncommands.getoutput('iptables -F')\ncommands.getoutput('setenforce 0')"

f = open("/var/www/html/sambclient.sh","w")
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
    <a href="/sambclient.sh" class="list-group-item"><b>Samba</b></a>
    <b>NOTE: AFTER DOWNLOADING THE FILE GIVE IT THE EXECUTION POWER</b>
  </div>
</div>

</body>
</html>
'''

print web
