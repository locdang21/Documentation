########## 
# Name : updateREP_Multi.py
# 
# Description
#       If the custom property in the resource environment variable does not exist it will be created.
#       If the custom property in the resource environment variable exist, it will be updated unless the value of the variable is the same.
#
# Direction:
#  1) Enter the Resource Environment Provider variable (myREP)
#  2) Update the repPropertyList with the properties for the Resource Environment Provider (name, value, type)
#  3) Run the wsadmin.sh command
#               wsadmin.sh -lang jython -f updateREP_Multi.py -user <WASADMIN> -password <WASPWD>
#       Example:
#               $WAS_PROFILE/bin/wsadmin.sh -lang jython -f updateREP_Multi.py -user wasadmin -password passw0rd
#
# Code used from the following link
#       https://codyburleson.com/display/blog/2013/02/17/How+to+create+custom+properties+for+a+resource+environment+provider+using+wasadmin+scripting
#
# Troubleshoot:
#  * If the Resource Environment Provider is newly created and does not have any properties, the script may throw an "null pointer exception because it can't find the property set id.  Manually add a new property.  You can delete the property after creating it if needed.
#  * If 2 different scrope has the same Resource Environment Provider name, update the variable theREP below in the script"
##########


# Set the Resource Environment Provider that will be updated
myREP=""

# List the property that needs to be updated or created
repPropertyList = [
{"name": "example.string", "value": "Update the string", "type": "java.lang.String", "desc": "String example"},
{"name": "example.integer", "value": "1", "type": "java.lang.Integer", "desc": "Integer example"},
{"name": "example.boolean", "value": "false", "type": "java.lang.Boolean", "desc": "Boolean example"}
]

# Check if the myREP variable has been set
if (myREP == ""):
   print ("ERROR: Update the variable myREP before continuing...")
   sys.exit(1)

# If 2 different scrope has the same Resource Environment Provider name, update the information below
#	* Point to the Server
#	* Point to the cluster
#

# Default: Find the Resource Environment Variable
theREP = AdminConfig.getid("/ResourceEnvironmentProvider:" + myREP)
#print theREP

# * Point to the Server
# wsadmin.sh -lang jython -f updateREP_Multi.py -user <WASADMIN> -password <WASPWD> -a <NODE> <SERVER>
# Example: wsadmin.sh -lang jython -f updateREP_Multi.py -user wasadmin -password passw0rd -a wpNode01 WebSphere_Portal
#
# Uncomment below:
#myCell=AdminControl.getCell()
#myNode=sys.argv[1]
#myServer=sys.argv[2]
#theREP = AdminConfig.getid("/Cell:" + myCell + "/Node:" + myNode + "/Server:" +  myServer + "/ResourceEnvironmentProvider:" + myREP)

# * Point to the cluster
# wsadmin.sh -lang jython -f updateREP_Multi.py -user <WASADMIN> -password <WASPWD> -a <CLUSTER>
# Example: wsadmin.sh -lang jython -f updateREP_Multi.py -user wasadmin -password passw0rd -a PortalCluster
#
# Uncomment below:
#myCell=AdminControl.getCell()
#myCluster=sys.argv[1]
#theREP = AdminConfig.getid("/Cell:" + myCell + "/ServerCluster:" + myCluster + "/ResourceEnvironmentProvider:" + myREP)

propSet = AdminConfig.showAttribute(theREP, 'propertySet')
#print propSet

resourceProperties = AdminConfig.list("J2EEResourceProperty", propSet).splitlines()

# Loop through the property files and compare the name and value of the property in the  Resource Environment Provider.
# If a match is found, either update it or leave it alone depending on the value of the property
# If no match is found, create the property
for property in repPropertyList:
   found = 0
   for resourceProperty in resourceProperties:
	if (AdminConfig.showAttribute(resourceProperty, "name") == property["name"]):
	   if (AdminConfig.showAttribute(resourceProperty, "value") != property["value"]):
		print "Found and modified: " + property["name"] + "=\"" + property["value"] + "\" in " + myREP
		AdminConfig.modify(resourceProperty, [['value', property["value"]]])
		AdminConfig.modify(resourceProperty, [['type', property["type"]]])
	   else:
		print "Found but did not modify: " + property["name"] + " in " + myREP
	   found =1
	   break
   if found ==0:
	print "Creating new property: " + property["name"] + "=\"" + property["value"] + "\" in " + myREP
	AdminConfig.create('J2EEResourceProperty', propSet, [["name", property["name"]], ["value", property["value"]], ["type", property["type"]], ["description", property["desc"]]])


# Save the changes
AdminConfig.save()
