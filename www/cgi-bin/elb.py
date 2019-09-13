#!/usr/bin/python2
import cgi,commands,time
print "content-type:text/html"
print ""
data=cgi.FieldStorage()
fld=data.keys()
k=len(fld)
r=''
p=1;
region="us-west-2a us-west-2b us-west-2c "
fld.sort()
name=data.getvalue(fld[0])
while p<k:
	r+=data.getvalue(fld[p])+' '
	p+=1

l=commands.getoutput(' sudo aws elb create-load-balancer --load-balancer-name '+name+' --listeners "Protocol=http,LoadBalancerPort=80,InstanceProtocol=http,InstancePort=80" --availability-zones '+region)


time.sleep(10)

a=commands.getoutput(' sudo aws elb register-instances-with-load-balancer --load-balancer-name '+name+' --instances '+r)

print l+'\n'
print a


