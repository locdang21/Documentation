########## 
# Name : createJ2EEAuth.py
#
# Example:
# $WP_PROFILE/bin/wsadmin.sh -lang jython -f scripts/createJ2EEAuth.py -user <WASADMIN> -password <WASPWD>
# 
# Description: The script will create a new J2EE Authentication data User
#
# Variables : Fill in the variables between the quotes under "Set Variables"
#	myAlias (required)
#	myUser (required)
#	myPassword (required)
#	myDescription 
#
##########

# Set Variables
myAlias=""
myUser=""
myPassword=""
myDescription="User created by script"

# Set JVM properties
iDetails = "-alias \"" + myAlias +"\" -user \"" + myUser + "\" -password \"" + myPassword + "\" -description \"" + myDescription + "\""

#print iDetails

# Create J2EE Authentication data User
AdminTask.createAuthDataEntry([iDetails])

# Save the changes
AdminConfig.save()