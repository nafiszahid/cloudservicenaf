#!/usr/bin/python2
import cgi,commands,time
print "content-type:text/html"
print ""
data=cgi.FieldStorage()
security=data.getvalue('secg')
snap=data.getvalue('sec')
num=data.getvalue('ni')

s=commands.getoutput("sudo aws ec2 create-security-group --group-name "+security+" --description 'security group for development environment in EC2' --query 'GroupId'")

commands.getoutput("sudo aws ec2 authorize-security-group-ingress --group-name "+security+" --protocol tcp --port 22 --cidr 0.0.0.0/0")

idd=commands.getoutput("sudo aws ec2 run-instances --image-id "+snap+" --security-group-ids "+s+" --count "+num+" --instance-type t2.micro --key-name devenv-key --query 'Instances[0].InstanceId'")

time.sleep(15)
p=commands.getoutput("sudo aws ec2 describe-instances --instance-ids "+idd+" --query 'Reservations[0].Instances[0].PublicIpAddress'")

msg = "IP-> "+p+"  Instance id-> "+idd

f = open("/var/www/html/fins1.sh","w")
f.write(msg)
f.close()

web='''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>AMAZON AWS</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/static/template1.css">
  <script src="/static/template2.js"></script>
  <script src="/static/template3.js"></script>
</head>
<body style="background-color:powderblue">
<div class="container">
  <h1 style="color:red">AMAZON AWS</h1>
  <div class="list-group">
    <h3>For LINUX instances:</h3>
    <a href="/fins1.sh" class="list-group-item"><b>Download the file of instructions</b></a>
    <a href="/devenv-key.pem" class="list-group-item" download><b>Download the key</b></a>
    <b>Open the terminal and type the command: ssh -i path_of_downloaded_key user_name@pulic_ip</b>
    <b>For Redhat : user_name= ec2-user</b>
    <b>For Ubuntu : user_name= ubuntu</b>
    <h3>For WINDOWS instances:</h3>
    <b>IP -> '''+p+'''</b>
    <b>Instance id -> '''+idd+'''</b>
    <p>Then follow the following steps:</p>
    <p>Open <b>Remote Desktop</b> Application</p>
    <p>Enter IP -> <b>'''+p+'''</b></p>
    <p>Log in as: <b>Administrator</b></p>
  </div>
</div>
</body>
</html>
'''

print web
