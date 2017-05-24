########## 
# Name : createSharedLib_node.py
#
# Example:
# $WP_PROFILE/bin/wsadmin.(bat/sh) -lang jython -f createSharedLib_node.py -user <WASADMIN> -password <WASPWD> -a <NODE_NAME>
# 
# Description: This script will create a new shared Library for a node

# Variable: Fill in the variables between the quotes under "Set Variables"
#	myLibName (required) = name
#	myNativePath = nativePath location - separated by a ;
#	myClassLoader = isolatedClassLoader (true/false) - default is false
#	myDescription = description
#	myClassPath (required) = classPath locations - separated by a ;
#
#
# NOTE: When using the script on windows use a '/' instead of '\' for all directroy structure
#
##########

# Set Variables
myLibName="WP NewLibrary"
myNativePath=""
myClassLoader="false"
myDescription="Description for the new Shared Library"
myClassPath=""

# Get Node and Cell
myNode=sys.argv[1]
myCell=AdminControl.getCell()

repWAS = AdminConfig.getid("/Cell:" + myCell + "/Node:" + myNode + "/")

# print repWAS

iDetails = "[[nativePath \"" + myNativePath + "\"] [name \"" + myLibName + "\"] [ isolatedClassLoader " + myClassLoader + "] [ description \"" + myDescription + "\"] [ classPath \"" + myClassPath +"\"]]" 

# print iDetails

# Create Shared Library
AdminConfig.create('Library', repWAS, iDetails) 


# Save the changes
AdminConfig.save()
