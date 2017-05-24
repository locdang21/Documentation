########## 
# Name : updateJVM_server.py
#
# $WAS_PROFILE/bin/wsadmin.(bat/sh) -lang jython -f updateJVM_server.py -user <WASADMIN> -password <WASPWD> -a <NODE_NAME> <SERVER_NAME>
#
# Example:
# /opt/IBM/WebSphere/wp_profile/bin/wsadmin.sh -lang jython -f updateJVM_server.py -user wasadmin -password passw0rd -a wpNode01 WebSphere_Portal
# 
# Description: This script will update the JVM of the server specified
#
# Variable: Only set the variables under "Set Variables" that needs to be updated.  Otherwise leave the variable "" unchanged.
#	myModeClass=(true/false)
#	myVerboseGC=(true/false)
#	myInitialHeap=integer
#	myMaximumHeap=integer
#	myRunHProf=(true/false)
#	myHprofArguments= 
#	myDebugMode=(true/false)
#	myDebugArgs=
#	myExecutableJarFileName=
#	myGenericJvmArguments=
#	myDisableJIT=(true/false)
#
#
# NOTE: 
#	When using the script on windows use a '/' instead of '\' for all directroy structure
#	If the script was ran and there was a mistake, run the command again with the correction
#
##########

# Set Variables
myVerboseModeClass=""
myVerboseGC=""
myVerboseModeJNI=""
myInitialHeap=""
myMaximumHeap=""
myRunHProf="" 
myHprofArguments="" 
myDebugMode=""
myDebugArgs=""
myExecutableJarFileName=""
myGenericJvmArguments=""
myDisableJIT=""

# Get Node and Server
myNode=sys.argv[1]
myServer=sys.argv[2]

iDetails = "-nodeName " + myNode + " -serverName " + myServer
print iDetails

# Set JVM properties
if myVerboseModeClass != "":
	iDetails = iDetails + " -verboseModeClass " + myVerboseModeClass 
if myVerboseGC != "":
	iDetails = iDetails + " -verboseModeGarbageCollection " + myVerboseGC
if myVerboseModeJNI != "":
	iDetails = iDetails + " -verboseModeJNI " + myVerboseModeJNI 
if myInitialHeap !="":
	iDetails = iDetails + " -initialHeapSize " + myInitialHeap
if myMaximumHeap !="":
	iDetails = iDetails + " -maximumHeapSize " + myMaximumHeap
if myRunHProf !="":
	iDetails = iDetails + " -runHProf " + myRunHProf
if myHprofArguments !="":
	iDetails = iDetails + " -hprofArguments " + myHprofArguments
if myDebugArgs !="":
	iDetails = iDetails + " -debugArgs \"" + myDebugArgs + "\" "
if myExecutableJarFileName !="":
	iDetails = iDetails + " -executableJarFileName \"" + myExecutableJarFileName + "\" "
if myGenericJvmArguments !="":
	iDetails = iDetails + " -genericJvmArguments \"" + myGenericJvmArguments + "\" "
if myDisableJIT !="":
	iDetails = iDetails + " -disableJIT \"" + myDisableJIT + "\" "

print iDetails

#Update JVM Properties
AdminTask.setJVMProperties([iDetails])

#Save changes
AdminConfig.save()