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
vg="myhd"

commands.getoutput("sudo lvextend --size +"+dirsize+"M /dev/mapper/"+vg+"-"+dirname)
commands.getoutput("sudo resize2fs /dev/mapper/"+vg+"-"+dirname)

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
    <h3>Size Extended</h3>
  </div>
</div>

</body>
</html>
'''

print web
