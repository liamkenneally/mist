class Organization(object):
    def __init__(self, session):
        super(Organization, self).__init__()
        self._session = session
        
#========================================================= TODO GETs ===============================================================#
# -- Update all the docstrings, they are currently copied from the Merkaki base docstring 
# -- Update all the metadata to ensure it is accurate
# update tags so that it represents the GUI for example for getSites() tags should be Organization > Site Configuration > Sites 
# With operation tag as: getSites


    def getCountryCodes(self):
        """
        **Get a list of supported country_codes for Mist APs**
        """

        metadata = {
            'tags': ['getSelf'],
            'operation': 'getSelf'
        }
        resource = f'/const/countries'

        return self._session.get(metadata, resource)
    
    
    def getsupportedChannels(self, **kwargs):
        """
        **Get a list of supported Mist AP Channels for selected country_code**
        - country_code (string): country code in two character (See ISO3166-1 alpha-2 for more details)
        https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['getsupportedChannels'],
            'operation': 'getsupportedChannels'
        }
        resource = f'/const/ap_channels'

        query_params = ['country_code']
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)


    def getSites(self, org_id):
        """
        **Get the sites that belong to a specific org_id**
        - org_id (string): (required)
        """

        metadata = {
            'tags': ['Organization', 'Site Confioguration', 'Sites'],
            'operation': 'getSites'
        }
        resource = f'/orgs/{org_id}/sites'

        return self._session.get(metadata, resource)
    
    
    def getSite(self, site_id):
        """
        **Get the site that belongs to the specific site_id**
        - site_id (string): (required)
        """

        metadata = {
            'tags': ['Organization', 'Site Confioguration', 'Sites', 'Site'],
            'operation': 'getSite'
        }
        resource = f'/sites/{site_id}'

        return self._session.get(metadata, resource)
    
    
    def getSiteStats(self, site_id):
        """
        **Get the site that belongs to the specific site_id**
        - site_id (string): (required)
        """

        metadata = {
            'tags': ['Organization', 'Site Confioguration', 'Sites', 'Site'],
            'operation': 'getSiteStats'
        }
        resource = f'/sites/{site_id}/stats'

        return self._session.get(metadata, resource)
    
 
    def getInventory(self, org_id, **kwargs):
        """
        **Get an Inventory of the Mist Dashboard. (Optional Filterable)**
        - org_id (string): (required)
        - model (string): (optional) Specify the model of device you wish to get e.g 'AP33'
        - serial (string): (optional) Specify the serial of a device you wish to get
        - magic (string): (optional) Specify the magic of a device you wish to get
        - site_id (string): (optional) Specify the site_id you would like to get a list of devices for
        - type (string): (optional) Specify the device type you would like to get e.g. 'ap' or 'switch'
        - mac (string): (optional) Specify the device mac that you would like to get e.g. 'a1ae23ace563'
        - vc_mac (string): (optional) Specify the virtual chassis mac that you would like to get e.g. 'a1ae23ace563'
        - vc (TBC): (optional): Not documented, but listed as a supported filter 
        - unassigned (TBC): (optional): Not documented, but listed as a supported filter 
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['getInventory'],
            'operation': 'getInventory'
        }
        resource = f'/orgs/{org_id}/inventory'

        query_params = ['model', 'serial', 'magic', 'site_id', 'type', 'mac', 'vc_mac', 'vc', 'unassigned']
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
    
    
    # TODO - Need to look at how to handle pagination 
    # Get Org Devices Stats


    def getAdmins(self, org_id):
        """
        **Get a list of admins for the org_id**
        - org_id (string): (required)
        """

        metadata = {
            'tags': ['getAdmins'],
            'operation': 'getAdmins'
        }
        resource = f'/orgs/{org_id}/admins'

        return self._session.get(metadata, resource)
    
    
    def getSelf(self):
        """
        **Get info on current authenticated user**
        """

        metadata = {
            'tags': ['getSelf'],
            'operation': 'getSelf'
        }
        resource = f'/self'

        return self._session.get(metadata, resource)
    
    
    def getAPITokens(self, org_id):
        """
        **Get a list of organisation API Tokens**
        - org_id (string): (required)
        """

        metadata = {
            'tags': ['getAPITokens'],
            'operation': 'getAPITokens'
        }
        resource = f'/orgs/{org_id}/apitokens'

        return self._session.get(metadata, resource)
    
    
    def getAPIToken(self, org_id, apitoken_id):
        """
        **Get a specific API Token by apitoken_id**
        - org_id (string): (required)
        - apitoken_id (string): (required)
        """

        metadata = {
            'tags': ['getAPIToken'],
            'operation': 'getAPIToken'
        }
        resource = f'/orgs/{org_id}/apitokens/{apitoken_id}'

        return self._session.get(metadata, resource)
    
    
    # Not a JSON respone, need to look further into how this works
    def getQRCodeForSDKInvite(self, org_id, sdkinvite_id):
        """
        **Get QR invite code for the SDK**
        - org_id (string): (required)
        - sdkinvite_id (string): (required)
        """

        metadata = {
            'tags': ['getAPIToken'],
            'operation': 'getAPIToken'
        }
        resource = f'/orgs/{org_id}/sdkinvites/{sdkinvite_id}/qrcode'

        return self._session.get(metadata, resource)
    
    
    def getLicenseSummary(self, org_id):
        """
        **Get a license summary for the org_id**
        - org_id (string): (required)
        """

        metadata = {
            'tags': ['getLicenseSummary'],
            'operation': 'getLicenseSummary'
        }
        resource = f'/orgs/{org_id}/licenses'

        return self._session.get(metadata, resource)
    
    
    def getLicenseUsageBySite(self, org_id):
        """
        **Get a license breakdown of usage by site**
        - org_id (string): (required)
        """

        metadata = {
            'tags': ['getLicenseUsageBySite'],
            'operation': 'getLicenseUsageBySite'
        }
        resource = f'/orgs/{org_id}/licenses/usages'

        return self._session.get(metadata, resource)  
    

    def getChangeLogs(self, org_id, **kwargs):
        """
        **Get Change logs for an org_id (Optional Filterable)**
        - org_id (string): (required)
        - start 
        - end
        - limit TODO - work out how limit will work with pagination
        - site_id (string): (optional) specify the site_id of the site you wish to filter
        - admin_name (string): (optional) admin name or email to filter on
        - message (string): (optional) message of the change log e.g. 'Accessed Org "LiamOrg"' 
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['getChangeLogs'],
            'operation': 'getChangeLogs'
        }
        resource = f'/orgs/{org_id}/logs'

        query_params = ['start', 'end', 'limit', 'site_id', 'admin_name', 'message']
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
    
    
    #Need to confirm if this is working properly with the params method...
    def getChangeLogCountByDistinctAttribute(self, org_id, **kwargs):
        """
        **Get a change log count by distinct attribute**
        - org_id (string): (required)
        - distinct (string): (optional) distinct can be admin_id | admin_name | message | site_id | default is adnin_name
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['getChangeLogCountByDistinctAttribute'],
            'operation': 'getChangeLogCountByDistinctAttribute'
        }
        resource = f'/orgs/{org_id}/logs'

        query_params = ['count?distinct']
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    
    def getOrgStats(self, org_id):
        """
        **Get the stats of the specified org_id**
        - org_id (string): (required)
        """

        metadata = {
            'tags': ['getOrgStats'],
            'operation': 'getOrgStats'
        }
        resource = f'/orgs/{org_id}/stats'

        return self._session.get(metadata, resource)  
    
    
    def getOrgSettings(self, org_id):
        """
        **Get the settings of the specified org_id**
        - org_id (string): (required)
        """

        metadata = {
            'tags': ['getOrgSettings'],
            'operation': 'getOrgSettings'
        }
        resource = f'/orgs/{org_id}/setting'

        return self._session.get(metadata, resource)  
    
    
    def getOrgCertificates(self, org_id):
        """
        **Get the certificate(s) for the specified org_id**
        -  (string): (required)
        """

        metadata = {
            'tags': ['getOrgCertficates'],
            'operation': 'getOrCertificates'
        }
        resource = f'/orgs/{org_id}/cert'

        return self._session.get(metadata, resource)  
    

# TODO Look at while this fails
    #def getOrgCRLFile(self, org_id):
    #    """
    #    **Return the DHCP subnet information for an appliance**
    #    https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets
    #    - serial (string): (required)
    #    """
#
    #    metadata = {
    #        'tags': ['getOrgCRLFile'],
    #        'operation': 'getOrCRLFile'
    #    }
    #    resource = f'/orgs/{org_id}/crl'
#
    #    return self._session.get(metadata, resource)  
    
    
     # TODO - Cannot test this without claiming a device. Come back to it later
    #Get List of Devices Recently Claimed


# TODO Needs further testing - Doesnt work
    def getAlarmTemplates(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getAlarmTemplates'],
            'operation': 'getAlarmTemplates'
        }
        resource = f'/installer/orgs/{org_id}/alarmtemplates'

        return self._session.get(metadata, resource)  
    

# TODO Needs further testing - Doesnt work
    def getSecurityPolicies(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getSecurityPolicies'],
            'operation': 'getSecurityPolicies'
        }
        resource = f'/installer/orgs/{org_id}/secpolicies'

        return self._session.get(metadata, resource) 
    
    

    def getRFTemplates(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getRFTemplates'],
            'operation': 'getRFTemplates'
        }
        resource = f'/orgs/{org_id}/rftemplates'

        return self._session.get(metadata, resource) 
    
    
    def getRFTemplate(self, org_id, rftemplate_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getRFTemplate'],
            'operation': 'getRFTemplate'
        }
        resource = f'/orgs/{org_id}/rftemplates/{rftemplate_id}'

        return self._session.get(metadata, resource) 
    
    
    def getNetworkTemplates(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getNetworkTemplates'],
            'operation': 'getNetworkTemplates'
        }
        resource = f'/orgs/{org_id}/networktemplates'

        return self._session.get(metadata, resource) 
    
    
    def getNetworkTemplate(self, org_id, networktemplate_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getNetworkTemplate'],
            'operation': 'getNetworkTemplate'
        }
        resource = f'/orgs/{org_id}/networktemplates/{networktemplate_id}'

        return self._session.get(metadata, resource) 


# ===== TODO Need to test this. Cannot find "AP Template in Mist Dash. Will need to create one via API when I get to POSTs" ======#
    def getAPTemplates(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getAPTemplates'],
            'operation': 'getAPTemplates'
        }
        resource = f'/orgs/{org_id}/aptemplates'

        return self._session.get(metadata, resource) 
    
    
    # ===== TODO Need to test this. Cannot find "AP Template" in Mist Dash. Will need to create one via API when I get to POSTs" ======#
    def getAPTemplate(self, org_id, aptemplate_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getAPTemplate'],
            'operation': 'getAPTemplate'
        }
        resource = f'/orgs/{org_id}/aptemplates/{aptemplate_id}'

        return self._session.get(metadata, resource) 


    # ===== TODO Need to test this. Cannot find "Networks" in Mist Dash. Will need to create one via API when I get to POSTs" ======#
    def getNetworks(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getNetworks'],
            'operation': 'getNetworks'
        }
        resource = f'/orgs/{org_id}/networks'

        return self._session.get(metadata, resource) 
    
    
# ===== TODO Need to test this. Cannot find "Networks" in Mist Dash. Will need to create one via API when I get to POSTs" ======#
    def getNetwork(self, org_id, network_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getNetwork'],
            'operation': 'getNetwork'
        }
        resource = f'/orgs/{org_id}/networks/{network_id}'

        return self._session.get(metadata, resource) 


# ===== TODO Need to test this. Cannot find "Gateways" in Mist Dash. Will need to create one via API when I get to POSTs" ======#
    def getGatewayTemplates(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getGatewayTemplates'],
            'operation': 'getGatewayTemplates'
        }
        resource = f'/orgs/{org_id}/gatewaytemplates'

        return self._session.get(metadata, resource) 
    
    
# ===== TODO Need to test this. Cannot find "Gateways" in Mist Dash. Will need to create one via API when I get to POSTs" ======# 
    def getGatewayTemplate(self, org_id, gatewaytemplate_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getGatewayTemplate'],
            'operation': 'getGatewayTemplate'
        }
        resource = f'/orgs/{org_id}/gatewaytemplates/{gatewaytemplate_id}'

        return self._session.get(metadata, resource) 
    
    
    def getDevices(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getDevices'],
            'operation': 'getDevices'
        }
        resource = f'/orgs/{org_id}/devices'

        return self._session.get(metadata, resource) 
    
    
    def getTemplates(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getTemplates'],
            'operation': 'getTemplates'
        }
        resource = f'/orgs/{org_id}/templates'

        return self._session.get(metadata, resource) 
    
    
# ===== TODO Need to test this. Cannot find "template_id" in Mist Dash. Will need to create one via API when I get to POSTs" ======#   
    def getTemplate(self, org_id, template_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getTemplate'],
            'operation': 'getTemplate'
        }
        resource = f'/orgs/{org_id}/templates/{template_id}'

        return self._session.get(metadata, resource) 
    

# =================================== TODO - Further testing required =========================================#
    def getAssetsStatus(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getAssetsStatus'],
            'operation': 'getAssetsStatus'
        }
        resource = f'/orgs/{org_id}/stats/assets/search'

        return self._session.get(metadata, resource)
    

# =================================== TODO - Further testing required =========================================#
    def getAssetStatus(self, org_id, mac):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getAssetStatus'],
            'operation': 'getAssetStatus'
        }
        resource = f'/orgs/{org_id}/stats/assets/search?mac="{mac}'

        return self._session.get(metadata, resource)
    
    
    # =================================== TODO - Further testing required =========================================#
    def getAssetsCount(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getAssetsCount'],
            'operation': 'getAssetsCount'
        }
        resource = f'/orgs/{org_id}/stats/assets/count'

        return self._session.get(metadata, resource)
    

    def getDeviceProfiles(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getDeviceProfiles'],
            'operation': 'getDeviceProfiles'
        }
        resource = f'/orgs/{org_id}/deviceprofiles'

        return self._session.get(metadata, resource)
    
    
    def getDeviceProfile(self, org_id, deviceprofile_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getDeviceProfiles'],
            'operation': 'getDeviceProfiles'
        }
        resource = f'/orgs/{org_id}/deviceprofiles/{deviceprofile_id}'

        return self._session.get(metadata, resource)


    def getPSK(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getDeviceProfiles'],
            'operation': 'getDeviceProfiles'
        }
        resource = f'/orgs/{org_id}/psks'

        return self._session.get(metadata, resource)
    
    
    def getGeneratedReports(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getGeneratedReports'],
            'operation': 'getGeneratedReports'
        }
        resource = f'/orgs/{org_id}/generated_reports'

        return self._session.get(metadata, resource)
    
    
    def getGeneratedReport(self, org_id, generated_report):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getGeneratedReports'],
            'operation': 'getGeneratedReports'
        }
        resource = f'/orgs/{org_id}/generated_reports/{generated_report}/download?fmt=pdf'

        return self._session.get(metadata, resource)
    
    
    # start=1546300800&end=-1d
    # start time seems to be in unix time format
    # Relative time supported? such as -1d, -2hr, -1w
    def getTickets(self, org_id, start_time, end_time):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getTickets'],
            'operation': 'getTickets'
        }
        resource = f'/orgs/{org_id}/tickets?start={start_time}&end={end_time}'

        return self._session.get(metadata, resource)
    
    
    def getTicketDetail(self, org_id, ticket_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getTicketDetail'],
            'operation': 'getTicketDetail'
        }
        resource = f'/orgs/{org_id}/tickets/{ticket_id}'

        return self._session.get(metadata, resource)
    
    
    def getSSOs(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getSSOs'],
            'operation': 'getSSOs'
        }
        resource = f'/orgs/{org_id}/ssos'

        return self._session.get(metadata, resource)
    
    
    def getSAMLMetadata(self, org_id, sso_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getSAMLMetadata'],
            'operation': 'getSAMLMetadata'
        }
        resource = f'/orgs/{org_id}/ssos/{sso_id}/metadata'

        return self._session.get(metadata, resource)
    
    
    # TODO - Needs further testing 
    # Need to test how the SDK handles an XML document. Currently, configured to parse json
    def getSAMLMetadataDownload(self, org_id, sso_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getSAMLMetadata'],
            'operation': 'getSAMLMetadata'
        }
        resource = f'/orgs/{org_id}/ssos/{sso_id}/metadata.xml'

        return self._session.get(metadata, resource)
    
    
    def getSSOFailures(self, org_id, sso_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getSSOFailures'],
            'operation': 'getSSOFailures'
        }
        resource = f'/orgs/{org_id}/ssos/{sso_id}/failures'

        return self._session.get(metadata, resource)
    
    
    def getSSORoles(self, org_id, sso_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getSSOFailures'],
            'operation': 'getSSOFailures'
        }
        resource = f'/orgs/{org_id}/ssos/{sso_id}/ssoroles'

        return self._session.get(metadata, resource)
    
    
    def getSubscriptions(self):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnetsr
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getSubscriptions'],
            'operation': 'getSubscriptions'
        }
        resource = f'/self/subscriptions'

        return self._session.get(metadata, resource)


    
###### Testing area ###  
    def getAssetsSearch(self, org_id: str, **kwargs):
        """
        **Get the sent and received bytes for each uplink of a network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-uplinks-usage-history
        - networkId (string): (required)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 days. The default is 10 minutes.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 600, 1800, 3600, 86400. The default is 60.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['getAssetsSearch', 'monitor', 'uplinks', 'usageHistory'],
            'operation': 'getAssetsSearch'
        }
        resource = f'/orgs/{org_id}/stats/assets/search'

        query_params = ['mac', 'start', 'end']
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
###### Testing area ###  


#==================================================== TODO POSTs ======================================================================#

    def createSite(self, org_id: str, name: str, notes: str, timezone: str, country_code: str, latlng: dict, 
                   address: str, sitegroup_ids: list, rftemplate_id: str, apporttemplate_id: str,
                   secpolicy_id: str, alarmtemplate_id: str, networktemplate_id: str, gatewaytemplate_id: str, **kwargs):
        """
        **Create a Site in the specified org_id**
        - org_id (string): (required)
        - name (string): (required) The name of the site
        - timezone (string): (optional) Timezone of the site
        - country_code (string): (optional) Country code for the site (For AP config generation), in two character
        - latlng (dict): (optional) Site location
            - lat (float): (optional) Latitude
            - lng (float): (optional) Longitude
        - address (string): (optional) Full address of the site
        - sitegroup_ids (list): (optional) List of sitegroups the site belongs to
        - rftemplate_id (string): (optional) RF Template ID, this takes precedence over Site Settings
        - apporttemplate_id (string): (optional) APPort Template ID
        - secpolicy_id (string): (optional) SecPolicy ID
        - alarmtemplate_id (string): (optional) Alarm Template ID, this takes precedence over the Org-level alarmtemplate_id
        - networktemplate_id (string): (optional) Network Template ID where site can use as its base Site Setting
        - gatewaytemplate_id (string): (optional) Gateway Template ID, used by gateways
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['createSite'],
            'operation': 'createSite'
        }
        resource = f'/orgs/{org_id}/sites'

        body_params = ['name', 'notes', 'timezone', 'country_code', 'latlng', 'address', 'sitegroup_ids', 'rftemplate_id', 
                       'apporttemplate_id', 'secpolicy_id', 'alarmtemplate_id', 'networktemplate_id', 'gatewaytemplate_id', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
    
    
    def AddInventory(self, org_id: str, ListOfClaimCodes: list, **kwargs):
        """
        **Add inventoy to the org_id**
        - org_id (string): (required)
        - listOfClaimCodes (list): A list of claim codes e.g ["AAAAA-AAAAAA-AAAAAA", "BBBBB-BBBBB-BBBBB"]
        """
        
        kwargs.update(locals())

        metadata = {
            'tags': ['AddInventory'],
            'operation': 'AddInventory'
        }
        resource = f'/orgs/{org_id}/inventory'

      
        payload = ListOfClaimCodes

        return self._session.post(metadata, resource, payload)
    
    
    def inviteAdmin(self, org_id: str, email: str, first_name: str, last_name: str, privileges: list, hours: int, **kwargs):
        """
        **Invite and Admin to the org_id**
        - org_id (string): (required)
        - email (string): (required) Email - admin_id is not exposed
        - first_name (string): (optional) First name, used in the invitation text
        - last_name (string): (optional) Last name
        - privileges (list): (optional) List of privileges the admin has on the orgs/sites
            - scope (string): (optional) site | org | sitegroup
            - role (string): (optional) admin | write | read | helpdesk
            - site_id (string): (optional) Site id
        - hours (int): (optional) How long the invite should be valid, default is 1 day. Max is capped at 1 week
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['inviteAdmin'],
            'operation': 'inviteAdmin'
        }
        resource = f'/orgs/{org_id}/invites'

        body_params = ['email', 'first_name', 'last_name', 'privileges', 'hours',]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
    
    
    def verifyToken(self, token: str, **kwargs):
        """
        **Verify a Token emailed to a user**
        - token (str): Token emailed to the user as part of the inviteAdmin()
        """
        
        kwargs.update(locals())

        metadata = {
            'tags': ['AddInventory'],
            'operation': 'AddInventory'
        }
        resource = f'/invite/verify/{token}'

      
        payload = None

        return self._session.post(metadata, resource, payload)
    
    
    def createAPIToken(self, org_id: str, name: str, privileges: list, **kwargs):
        """
        **Create an API Token for a specific Org/Site with required Privileges**
        - org_id (string): (required)
        - name (string): (optional) Name of the API Token
        - privileges (list): (optional) List of privileges the token has on the orgs/sites
            - scope (string): (optional) site | org | sitegroup
            - role (string): (optional) admin | write | read 
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['createAPIToken'],
            'operation': 'createAPIToken'
        }
        resource = f'/orgs/{org_id}/apitokens'

        body_params = ['name', 'privileges']
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
    
    
    # WIP
    def createSDKInvite(self, org_id: str, name: str, quota_limited: bool, quota: int, enabled: bool, **kwargs):
        """
        **Create an SDK Invite**
        - org_id (string): (required)
        - name (string): (optional) Name of the API Token
        - privileges (list): (optional) List of privileges the token has on the orgs/sites
            - scope (string): (optional) site | org | sitegroup
            - role (string): (optional) admin | write | read 
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['createSDKInvite'],
            'operation': 'createSDKInvite'
        }
        resource = f'/orgs/{org_id}/sdkinvites'

        body_params = ['name', 'quota_limited', 'quota', 'enabled']
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
    
    # POST /api/v1/orgs/:org_id/sdkinvites/:sdkinvite_id/email
    # POST /api/v1/orgs/:org_id/sdkinvites/:sdkinvite_id/sms
    # POST /api/v1/mobile/verify/:secret
    # POST /api/v1/orgs/:org_id/sdktemplates
    
    
    def claimOrderByActivationCode(self, org_id: str, code: str, type: str, **kwargs):
        """
        **Create an SDK Invite**
        - org_id (string): (required)
        - code (string): (required) Activation code e.g. 'AAAAA-BBBBB-CCCCC-DDDDD'
        - type (string): (optional) what to claim, license |inventory | all (default)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['claimOrderByActivationCode'],
            'operation': 'claimOrderByActivationCode'
        }
        resource = f'/orgs/{org_id}/claim'

        body_params = ['code', 'type']
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
    
    
    def createOrg(self, name: str, session_expiry: int, alarmtemplate_id: str, orggroup_id: list, allow_mist: bool, **kwargs):
        """
        **Create a new Org**
        - name (string): (optional) org name
        - session_expiry (int): (optional) how long the login session should last, in minutes, default is 1440 (24 hours), between 10 (min) and 20160 (2 weeks)
        - alarmtemplate_id (string): (optional) Alarm Template ID, the default Alarm Template to use for the Org, can be override by Site
        - orggroup_ids (list): (optional) list of OrgGroup ids
        - allow_mist (bool): (optional) whether to allow Mist to look at this org, default is True
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['createOrg'],
            'operation': 'createOrg'
        }
        resource = f'/orgs'

        body_params = ['name', 'session_expiry', 'alarmtemplate_id', 'orggroup_ids', 'allow_mist']
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
    
    
    def cloneOrg(self, org_id: str, name: str, **kwargs):
        """
        **Create an Org by cloning from another one. Org Settings, Templates, Device Profiles, Alarm Templates, RFTemplates, Security Policies, Wxlan Tags, Wxlan Tunnels,
        Wxlan Rules, Org Wlans will be copied. Sites and Site Groups will not be copied, and therefore, the copied template will not be applied to any site/sitegroups.**
        - org_id (string): required
        - name (string): (optional) New org name
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['cloneOrg'],
            'operation': 'cloneOrg'
        }
        resource = f'/orgs/{org_id}/clone'

        body_params = ['name']
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
    
    
    # POST /api/v1/orgs/:org_id/setting/pcap_bucket/setup
    # POST /api/v1/orgs/:org_id/setting/pcap_bucket/verify
    
    
    
    
    
    
    
    
    
    
    #==================================================== TODO PUTs ======================================================================#
    
    #==================================================== TODO PATCHs ======================================================================#
    
    #==================================================== TODO DELETEs ======================================================================#
    
    def deleteSite(self, site_id: str):
        """
        **Delete a Site**
        - site_id (string): (required)
        """

        metadata = {
            'tags': ['deleteSite'],
            'operation': 'deleteSite'
        }
        resource = f'/sites/{site_id}'

        return self._session.delete(metadata, resource)

    
    def deleteAdmin(self, org_id: str, admin_id: str):
        """
        **Delete an invited Admin**
        - org_id (string): (required)
        - admin_id (string): (required)
        """

        metadata = {
            'tags': ['deleteAdmin'],
            'operation': 'deleteAdmin'
        }
        resource = f'/orgs/{org_id}/admins/{admin_id}'

        return self._session.delete(metadata, resource)
    
    
    def deleteInvitedAdmin(self, org_id: str, invite_id: str):
        """
        **Delete an invited Admin**
        - org_id (string): (required)
        - invite_id (string): (required)
        """

        metadata = {
            'tags': ['deleteInvitedAdmin'],
            'operation': 'deleteInvitedAdmin'
        }
        resource = f'/orgs/{org_id}/invites/{invite_id}'

        return self._session.delete(metadata, resource)
    
    
    def deleteAPIToken(self, org_id: str, apitoken_id: str):
        """
        **Delete an API Token**
        - org_id (string): (required)
        - apitoken_id (string): (required)
        """

        metadata = {
            'tags': ['deleteAPIToken'],
            'operation': 'deleteAPIToken'
        }
        resource = f'/ orgs/{org_id}/apitokens/{apitoken_id}'

        return self._session.delete(metadata, resource)