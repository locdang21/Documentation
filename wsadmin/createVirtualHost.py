########## 
# Name : createVirtualHost.py
#
# $WAS_PROFILE/bin/wsadmin.(bat/sh) -lang jython -f createVirtualHost.py -user <WASADMIN> -password <WASPWD> -a <HOST> <PORT>
#
# Example:
# wsadmin.(bat/sh) -lang jython -f createVirtualHost.py -user wasadmin -password passw0rd -a "*" 80
# wsadmin.(bat/sh) -lang jython -f createVirtualHost.py -user wasadmin -password passw0rd -a myhost.loc.com 80
#
# Description: The script will create a new virtual host in the default_host
#
##########

myHost=sys.argv[1]
myPort=sys.argv[2]
myCell=AdminControl.getCell()

if (myPort.isdigit()==0):
   print "ERROR: If the hostname is *, make sure it is surrounded by quotes"
   print "ERROR: Check port number"
   print "Example: wsadmin.(bat/sh) -lang jython -f createVirtualHost.py -user wasadmin -password passw0rd -a \"*\" 80"
   sys.exit(1)

cellID=AdminConfig.getid("/Cell:" + myCell + "/VirtualHost:default_host/")
#print cellID

theSettings = "[[hostname " + myHost + "] [port " + myPort + "]]"
#print theSettings

#AdminConfig.create('HostAlias', cellID, '[[hostname myHost] [port myPort]]')
AdminConfig.create('HostAlias', cellID, theSettings)

print "SUCCESS: Virtual Host Created: " + myHost + "=" + myPort

# Uncomment if you want to list all of the Virtual host for the default_host
#AdminConfig.list('HostAlias', AdminConfig.getid( '/Cell:dmgrCell01/VirtualHost:default_host/')) 

#Save changes
AdminConfig.save()
