##########
#
# Author: Loc Dang
#
# Direction: 
#  1) Copy and extract the following file from your WebSphere Portal Server to your local linux environment
#	<WP_HOME>/scriptingportlet/wp.scriptportlet.cmdln/bin/sp_cmdln.zip
#
#	Example: /opt/IBM/WebSphere/PortalServer/scriptingportlet/wp.scriptportlet.cmdln/bin/sp_cmdln.zip	
#
#  2) Update <SP_CMDLN>/sp-config.json with the following information
#	"scriptPortletServer": "https://<host>:<port>",
#	"laxSSL": <true|false>,
#	"performAuth": <true|false>,
#	"portalUser": "<value>",
#	"portalPassword": "<value>",
#	
#	If context root was changed then the following variables will need to be updated
#	"contenthandlerPath": "/wps/mycontenthandler",
#
#  3) Copy spPushMulti.sh to your local file system
#
#  4) Run the following command to push multiple Script Portlet/Application
#	spPushMulti.sh -spDir <Diriectory of sp.sh binary> -spContent <Directory of SP content>
# 
#	Example:   spPushMulti.sh -spDir /opt/tmp/sp_cmdln -spContent /opt/tmp/sp_samples/
#
# NOTE: 
#	* If -spDir or -spContent is not used then the current location will be used.
#	* For each script portlet directory make sure that the sp-config.json contains "wcmContentName" variable.  
#		Example: { "wcmContentName": "Hello World" }.  
#	* The script will not work for virtual portals
#
#########


while [[ $# -gt 1 ]]
do
key="$1"

case $key in
  -spDir)
  spDir="$2"
  shift #
  ;;
  -spContent)
  spContent="$2"
  shift #
  ;;
esac
shift #
done

if [ -z $spContent ]
then
  spContent="."
fi

if [ -z $spDir ]
then
  spDir="."
fi

echo Script Portlet sp directory is ${spDir};
echo Script Portlet content directory is ${spContent};

for f in $spContent/*/;
do
 echo pushing $f;
 $spDir/sp.sh push -contentRoot $f
done
