########## 
# Name : createREP_cluster.py
#
# Example:
# $WP_PROFILE/bin/wsadmin.sh -lang jython -f scripts/createREP_cluster.py -user <WASADMIN> -password <WASPWD> -a <CLUSTER_NAME>
# 
# Description: The script will create a new Resource Environment Provider for a cluster scope
#
# Variables : Fill in the variables between the quotes under "Set Variables"
#	myRepName (Required)= Resource Environment provider Name
#	myDescription = Description of the Resource Environment Provider
#
##########

# Set Variables
myREPName="newREP"
myDescription="Fill in a description"

# Get WAS PATH
myCell=AdminControl.getCell()
myCluster=sys.argv[1]

repWAS = AdminConfig.getid("/Cell:" + myCell + "/ServerCluster:" + myCluster + "/")

# print repWAS

# Details for the Resource Environemnt Provider
iDetails = "[[name \"" + myREPName +"\"] [ description \"" + myDescription + "\"]]" 

# print iDetails

#Create Resource Environment Provider
AdminConfig.create('ResourceEnvironmentProvider', repWAS, iDetails ) 

# Save the changes
AdminConfig.save()



