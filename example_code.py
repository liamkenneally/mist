from mist import *


# Create a Mist Dashboard Session
dashboard = DashboardAPI(api_key=config.API_KEY_ENVIRONMENT_VARIABLE)


# Call the getSelf() method from the Sites Class 
# Extract the Mist org_id for future use in the script
mist_self = dashboard.sites.getSelf()
org_id = mist_self["privileges"][0]["org_id"]


# Call the getSites() method from the Sites Class
# Extract the required Mist site_id for future use in the script
mist_site = dashboard.sites.getSites(org_id)
site_id = mist_site[0]["id"]


# get RFTemplate & NetworkTemplate for site creation later in script
rftemp = dashboard.sites.getRFTemplates(org_id)
rftemplate_id = rftemp[0]["id"]
nwtemp = dashboard.sites.getNetworkTemplates(org_id)
networktemplate_id = nwtemp[0]["id"]


# Create a Mist Site
create_examplesite = dashboard.sites.createSite(org_id, 
                                                "Test Site by API", 
                                                "Created via Python API - final test", 
                                                "Europe/London",
                                                "GB", {'lat': 51.482802, 'lng': 0.028545 },
                                                 "12 My Street, My Town, My City, UK, SE1 1AB",
                                                 51.482802, 0.028545, [],
                                                 rftemplate_id, '', '', '', networktemplate_id, '')
print(create_examplesite)
