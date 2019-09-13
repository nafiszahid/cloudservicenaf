#!/usr/bin/python2
import cgi
print "content-type:text/html"
print ""
data=cgi.FieldStorage()
user=data.getvalue('username')
password=data.getvalue('password')
web='''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Cloud Computing</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/static/template1.css">
  <script src="/static/template2.js"></script>
  <script src="/static/template3.js"></script>
</head>
<body style="background-color:powderblue">
<div class="container">
  <h1 style="color:red">Cloud Computing</h1>
  <div class="list-group">
    <a href="/saas.html" class="list-group-item"><b>SAAS  ->  Software as a service</b></a>
    <a href="/staas.html" class="list-group-item"><b>StAAS ->  Storage as a service</b></a>
    <a href="/iaas.html" class="list-group-item"><b>IAAS  ->  Infrastructure as a service</b></a>
    <a href="/paas.html" class="list-group-item"><b>PAAS  ->  Platform as a service</b></a>
    <a href="/amazon.html" class="list-group-item"><b>AMAZON AWS</b></a>
  </div>
</div>

</body>
</html>
'''

if user=='manka' and password=='hello':
	print web
else:
	print 'Invalid Entry!!!'
