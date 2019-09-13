#!/usr/bin/python2
import cgi,commands,time
print "content-type:text/html"
print ""
data=cgi.FieldStorage()
a=data.getvalue('vid')
b=data.getvalue('iid')
c=data.getvalue('nv')
d=data.getvalue('size')

if size="":
	l=commands.getoutput("sudo aws ec2 attach-volume --volume-id "+a+" --instance-id "+b+" --device /dev/"+c)
else:
	lm=commands.getoutput("sudo aws ec2 modify-volume --region us-west-2 --volume-id "+a+" --size "+d+" --volume-type gp2")
	l=commands.getoutput("sudo aws ec2 attach-volume --volume-id "+a+" --instance-id "+b+" --device /dev/"+c)


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
   <h3>VOLUME ATTACHED</h3>
   <p>For LINUX instances:</p>
   <p>Create a directory inside <b>/media</b></p>
   <p>Format it</p>
   <p>Mount</p>
   <p>Mount as -> <b>mount /dev/'''+name+''' /media/directory_name</b></p>
  </div>
</div>

</body>
</html>
'''

print web
