from mist import *


dash = DashboardAPI(api_key=config.API_KEY_ENVIRONMENT_VARIABLE)
doc = dash.organization.getSelf()
org_id = doc["privileges"][0]["org_id"]



test = dash.organization.getSites(org_id)
site_id = test[0]["id"]

#test2 = dash.organization.getSite(site_id)
#print(test2)



test2 = dash.organization.getInventory(org_id)
site_id = test2[0]["site_id"]


test3 = dash.organization.getSite(site_id)



test4 = dash.organization.getSiteStats(site_id)



test5 = dash.organization.getAdmins(org_id)


test6 = dash.organization.getAPITokens(org_id)



test7 = dash.organization.getLicenseSummary(org_id)

test8 = dash.organization.getLicenseUsageBySite(org_id)



test9 = dash.organization.getChangeLogs(org_id)


test10 = dash.organization.getOrgStats(org_id)


test11 = dash.organization.getOrgSettings(org_id)

test12 = dash.organization.getOrgCertificates(org_id)

# FAILED 
#test13 = dash.organization.getOrgCRLFile(org_id)
#print(test13)

#test14 = dash.organization.getTest(org_id)
#print(test14)

# TODO Needs further testing
#test15 = dash.organization.getListofAlarmTemplates(org_id)

# TODO Needs further testing
#test16 = dash.organization.getListofSecurityPolicies(org_id)
#print(test16)


test17 = dash.organization.getRFTemplates(org_id)
rftemplate_id = test17[0]["id"]

test18 = dash.organization.getRFTemplate(org_id, rftemplate_id)


test19 = dash.organization.getNetworkTemplates(org_id)
networktemplate_id = test19[0]["id"]


test20 = dash.organization.getNetworkTemplate(org_id, networktemplate_id)

# WORKS FINE
#test21 = dash.organization.createSite(org_id, "Test Site by API", "Crreated via Python API - final test", "Europe/London", "GB", {}, "35 Tallis Grove, London SE7 7FL, UK", 0, 0, [], rftemplate_id, '', '', '', '', '')
#print(test21)

test21 = dash.organization.getDevices(org_id)


test22 = dash.organization.getTemplates(org_id)


#test23 = dash.organization.getNetworkTemplate(org_id, template_id)
#print(test23)


test24 = dash.organization.getAssetsCount(org_id,)


test25 = dash.organization.getDeviceProfiles(org_id)


test26 = dash.organization.getPSK(org_id)

test27 = dash.organization.getCountryCodes()

test28 = dash.organization.getsupportedChannels(country_code='GB')


test29 = dash.organization.getInventory(org_id)


test30 = dash.organization.getAdmins(org_id)




test31 = dash.organization.AddInventory(org_id, ListOfClaimCodes=["SXT2F-DW9TJ-SKWEQ", "AAAAA-AAAAA-AAAAA"])



#test32 = dash.organization.inviteAdmin(org_id, email="liamkenneally469@gmail.com", first_name="Liam", last_name="K", hours=4, privileges=[{'scope': 'org', 'role': 'admin'}])
#print(test32)

#test34 = dash.organization.getAdmins(org_id)
#print(test34)

#test33 = dash.organization.deleteInvitedAdmin(org_id, invite_id="9c16d84f-1487-424c-9cf7-5309d11a9561")
#print(test33)

#test34 = dash.organization.getAdmins(org_id)
#print(test34)


#test35 = dash.organization.getSites(org_id)

#test36 = dash.organization.deleteSite(site_id="5ea92060-4650-416d-be12-1a01bf38e176")
#print(test36)

#test37 = dash.organization.deleteAdmin(org_id, admin_id="09bf26b5-f716-4106-93b7-5f9f221c0d2f")
#print(test37)

#test38 = dash.organization.createAPIToken(org_id, "Test_API_KEY", privileges=[{'scope':'org', 'role':'admin'}])
#print(test38)

#test39 = dash.organization.getAPITokens(org_id)
#print(test39)

#test40 = dash.organization.deleteAPIToken(org_id, apitoken_id='2114283e-80ad-40e5-bb2a-8c6e75bd8cde')


