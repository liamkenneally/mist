class Organization(object):
    def __init__(self, session):
        super(Organization, self).__init__()
        self._session = session
        
#========================================================= TODO GETs ===============================================================#
# -- Update all the docstrings, they are currently copied from the Merkaki base docstring 
# -- Update all the metadata to ensure it is accurate
# update tags so that it represents the GUI for example for getSites() tags should be Organization > Site Configuration > Sites 
# With operation tag as: getSites

    def getSelf(self):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getSelf'],
            'operation': 'getSelf'
        }
        resource = f'/self'

        return self._session.get(metadata, resource)


    def getSites(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets
        - serial (string): (required)
        """

        metadata = {
            'tags': ['Organization', 'Site Confioguration', 'Sites'],
            'operation': 'getSites'
        }
        resource = f'/orgs/{org_id}/sites'

        return self._session.get(metadata, resource)
    
    
    def getSite(self, site_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getSite'],
            'operation': 'getSite'
        }
        resource = f'/sites/{site_id}'

        return self._session.get(metadata, resource)
    
    
    def getSiteStats(self, site_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getSite', 'stats'],
            'operation': 'getSiteStats'
        }
        resource = f'/sites/{site_id}/stats'

        return self._session.get(metadata, resource)
    
    
    
    def getInventory(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getInventory'],
            'operation': 'getInventory'
        }
        resource = f'/orgs/{org_id}/inventory'

        return self._session.get(metadata, resource)
    
    
    # TODO - Need to look at how to handle pagination 
    # Get Org Devices Stats


    def getAdmins(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getAdmins'],
            'operation': 'getAdmins'
        }
        resource = f'/orgs/{org_id}/admins'

        return self._session.get(metadata, resource)
    
    
    def getAPITokens(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getAPITokens'],
            'operation': 'getAPITokens'
        }
        resource = f'/orgs/{org_id}/apitokens'

        return self._session.get(metadata, resource)
    
    
   
    # Get API Token
    
    
    def getLicenseSummary(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getLicenseSummary'],
            'operation': 'getLicenseSummary'
        }
        resource = f'/orgs/{org_id}/licenses'

        return self._session.get(metadata, resource)
    
    
    def getLicenseUsageBySite(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getLicenseUsageBySite'],
            'operation': 'getLicenseUsageBySite'
        }
        resource = f'/orgs/{org_id}/licenses/usages'

        return self._session.get(metadata, resource)  
    

    def getChangeLogs(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getChangeLogs'],
            'operation': 'getChangeLogs'
        }
        resource = f'/orgs/{org_id}/logs'

        return self._session.get(metadata, resource)  
    
    
    def getOrgStats(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getOrgStats'],
            'operation': 'getOrgStats'
        }
        resource = f'/orgs/{org_id}/stats'

        return self._session.get(metadata, resource)  
    
    
    def getOrgSettings(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets
        - serial (string): (required)
        """

        metadata = {
            'tags': ['getOrgSettings'],
            'operation': 'getOrgSettings'
        }
        resource = f'/orgs/{org_id}/setting'

        return self._session.get(metadata, resource)  
    
    
    def getOrgCertificates(self, org_id):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets
        - serial (string): (required)
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






#==================================================== TODO POSTs ======================================================================#

    def createSite(self, org_id: str, name: str, notes: str, timezone: str, country_code: str, latlng: dict, 
                   address: str, lat: float, lng: float, sitegroup_ids: list, rftemplate_id: str, apporttemplate_id: str,
                   secpolicy_id: str, alarmtemplate_id: str, networktemplate_id: str, gatewaytemplate_id: str, **kwargs):
        """
        **Add a static route for an MX or teleworker network**
        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-static-route
        - networkId (string): (required)
        - name (string): The name of the new static route
        - subnet (string): The subnet of the static route
        - gatewayIp (string): The gateway IP (next hop) of the static route
        - gatewayVlanId (string): The gateway IP (next hop) VLAN ID of the static route
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'staticRoutes'],
            'operation': 'createNetworkApplianceStaticRoute'
        }
        resource = f'/orgs/{org_id}/sites'

        body_params = ['name', 'notes', 'timezone', 'country_code', 'latlng', 'address', 'lat', 'lng', 'sitegroup_ids', 'rftemplate_id', 
                       'apporttemplate_id', 'secpolicy_id', 'alarmtemplate_id', 'networktemplate_id', 'gatewaytemplate_id', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
    
    
    #==================================================== TODO PUTs ======================================================================#
    
    #==================================================== TODO PATCHs ======================================================================#
    
    #==================================================== TODO DELETEs ======================================================================#