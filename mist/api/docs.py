class Docs(object):
    def __init__(self, session):
        super(Docs, self).__init__()
        self._session = session
        


    def getAPIDocs(self):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets
        - serial (string): (required)
        """

        metadata = {
            'tags': ['self'],
            'operation': 'getSelf'
        }
        resource = f'/self'

        return self._session.get(metadata, resource)