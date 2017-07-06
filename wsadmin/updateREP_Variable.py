########## 
# Name : updateREP_Variable.py
# 
# Description
#       If the custom property in the resource environment variable does not exist it will be created.
#       If the custom property in the resource environment variable exist, it will be updated unless the value of the variable is the same.
#
# Direction:
#  1) Update the Set Variables section (Required: myREP, myName, myValue)(Optional: myType, myDescription, myReq)
#  2) Run the wsadmin.sh command
#               wsadmin.sh -lang jython -f updateREP_Variable_server.py -user <WASADMIN> -password <WASPWD>
#       Example:
#               $WAS_PROFILE/bin/wsadmin.sh -lang jython -f updateREP_Variable.py -user wasadmin -password passw0rd
#
# Code used from the following link
#       https://codyburleson.com/display/blog/2013/02/17/How+to+create+custom+properties+for+a+resource+environment+provider+using+wasadmin+scripting
#
# Troubleshoot:
#  If the Resource Environment Provider is newly created and does not have any properties, the script may throw an "null pointer exception because it can't find the property set id.  Manually add a new property.  You can delete the property after creating it if needed.
##########

# Set Variables
myREP=""
myName=""
myValue=""
myType="java.lang.String"
myDesc="Created/Updated by updateREP_Variable.py"
myReq="false"

# Check the required variables: myREP and myName
# If creating a new variable then type is required and defaulted to String
if (myREP == ""):
   print ("ERROR: Update the variable myREP before continuing...")
   sys.exit(1)

if (myName == ""):
   print ("ERROR: Update the variable myName before continuing...")
   sys.exit(1)

# Get the ID for the Resource Environment Variable
theREP = AdminConfig.getid("/ResourceEnvironmentProvider:" + myREP)
#print theREP

# Get all the variables in the Resource Environment Variable
propSet = AdminConfig.showAttribute(theREP, 'propertySet')
#print propSet

resourceProperties = AdminConfig.list("J2EEResourceProperty", propSet).splitlines()
#print resourceProperties


# Go through the list of properties to find a match.  If it was not found, create it.
found = 0
for resourceProperty in resourceProperties:
   if (AdminConfig.showAttribute(resourceProperty, "name") == myName):
        if (AdminConfig.showAttribute(resourceProperty, "value") != myValue):
           print("Found and modified: " + myName + "=" + myValue + " in " + myREP)
           AdminConfig.modify(resourceProperty, [['value', myValue]])
        else:
           print("Found but did not modify: " + myName + " in " + myREP)
        found =1
        break
if found == 0:
   print ("Creating new property: " + myName + "=" + myValue + " in " + myREP)
   AdminConfig.create('J2EEResourceProperty', propSet, [["name", myName], ["value", myValue], ["type", myType], ["description", myDesc], ["required", myReq]])


# Save the changes
AdminConfig.save()

