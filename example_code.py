from mist import *


dash = DashboardAPI(api_key=config.API_KEY_ENVIRONMENT_VARIABLE)
doc = dash.docs.getAPIDocs()
doc1 = dash.docs.getAPIDocs()
org_id = doc["privileges"][0]["org_id"]



test = dash.sites.getSites(org_id)
site_id = test[0]["id"]

#test2 = dash.sites.getSite(site_id)
#print(test2)



test2 = dash.sites.getInventory(org_id)
site_id = test2[0]["site_id"]


test3 = dash.sites.getSite(site_id)



test4 = dash.sites.getSiteStats(site_id)



test5 = dash.sites.getAdmins(org_id)


test6 = dash.sites.getAPITokens(org_id)



test7 = dash.sites.getLicenseSummary(org_id)

test8 = dash.sites.getLicenseUsageBySite(org_id)



test9 = dash.sites.getChangeLogs(org_id)


test10 = dash.sites.getOrgStats(org_id)


test11 = dash.sites.getOrgSettings(org_id)

test12 = dash.sites.getOrgCertificates(org_id)

# FAILED 
#test13 = dash.sites.getOrgCRLFile(org_id)
#print(test13)

#test14 = dash.sites.getTest(org_id)
#print(test14)

# TODO Needs further testing
#test15 = dash.sites.getListofAlarmTemplates(org_id)

# TODO Needs further testing
#test16 = dash.sites.getListofSecurityPolicies(org_id)
#print(test16)


test17 = dash.sites.getRFTemplates(org_id)
rftemplate_id = test17[0]["id"]

test18 = dash.sites.getRFTemplate(org_id, rftemplate_id)


test19 = dash.sites.getNetworkTemplates(org_id)
networktemplate_id = test19[0]["id"]


test20 = dash.sites.getNetworkTemplate(org_id, networktemplate_id)

# WORKS FINE
#test21 = dash.sites.createSite(org_id, "Test Site by API", "Crreated via Python API - final test", "Europe/London", "GB", {}, "35 Tallis Grove, London SE7 7FL, UK", 0, 0, [], rftemplate_id, '', '', '', '', '')
#print(test21)
