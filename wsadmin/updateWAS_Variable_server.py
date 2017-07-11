########## 
# Name : updateWAS_Variable_server.py
# 
# Description
#       If the WAS variable does not exist it will be created.
#       If the WAs variable exist, it will be updated unless the value of the variable is the same.
#
# Direction:
#  1) Update the wasVariableList in the script below
#  2) Run the following wsadmin command to update/create the WAS variable at the server level
# 
# wsadmin.sh -lang jython -f updateWAS_Variable_server.py -user <WASADMIN> -password <WASPWD> -a <NODE> <SERVER>
# Example: 
#	wsadmin.sh -lang jython -f updateWAS_Variable_server.py -user wasadmin -password passw0rd -a wpNode01 WebSphere_Portal
#	wsadmin.sh -lang jython -f updateWAS_Variable_server.py -user wasadmin -password passw0rd -a wpNode01 nodeagent
#	wsadmin.sh -lang jython -f updateWAS_Variable_server.py -user wasadmin -password passw0rd -a dmgrNode01 dmgr
#
##########

wasVariableList = [
{"name": "example.var1", "value": "value1", "desc": "description for example 1"},
{"name": "example.var2", "value": "value2", "desc": "description for example 2"},
{"name": "WCM_SCHEMA", "value": "jcr", "desc": "description for example 3"}
]

myCell=AdminControl.getCell()
myNode=sys.argv[1]
myServer=sys.argv[2]

# Create the variable for the scope
wasScope = AdminConfig.getid("/Cell:" + myCell + "/Node:" + myNode + "/Server:" +  myServer + "/")
#print wasScope

# Store the list of environment variables 
wasVariables=AdminConfig.list('VariableSubstitutionEntry', wasScope).splitlines()
#print wasVariables

# Create the Environment variable mapping location
varMap="(cells/" + myCell + "/nodes/" + myNode + "/servers/" + myServer + "|variables.xml#VariableMap_1)"

# Check each variable for a match.  If it matched it will determine it it will update it or leave it alone by the value
# If it does not exist, it will create it.
for property in wasVariableList:
   found = 0
   for entries in wasVariables:
        if (AdminConfig.showAttribute(entries, "symbolicName") == property["name"]):
           if (AdminConfig.showAttribute(entries, "value") != property["value"]):
              print "Found and modified: " + property["name"] + "=\"" + property["value"] + "\""
              AdminConfig.modify(entries, [['value', property["value"]]])
              AdminConfig.modify(entries, [['description', property["desc"]]])
           else:
              print "Found but did not modify: " + property["name"]
           found =1
           break
   if found ==0:
      print "Creating new property: " + property["name"] + "=\"" + property["value"] + "\""
      varName="\"" + property["name"] +"\""
      varValue="\"" + property["value"] + "\""
      varDesc="\"" + property["desc"] + "\""
      #print varName
      #print varValue
      #print varDesc
      varEntry= "[[\"symbolicName\" " + varName + "] [\"value\" " + varValue + "] [\"description\" " + varDesc + "]]"
      #print varEntry
      AdminConfig.create('VariableSubstitutionEntry', varMap, varEntry)

# Save the changes
AdminConfig.save()

