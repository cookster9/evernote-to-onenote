#create_secion_pages

import msal
import jwt
import json
import sys
import requests
from datetime import datetime

import re

import PASS

graphURI = 'https://graph.microsoft.com/'

def parse_token(full_token):
    p = re.search('=(.*?)&', full_token) #regex for between = and &. re.search gets the values between
    return p.group(1)

def msgraph_request(resource, requestHeaders):
    # Request
    results = requests.get(resource, headers=requestHeaders).json()
    return results

def main():
    full_token_url = PASS.token_current
    token_parsed = parse_token(full_token_url)
    accessToken = {'Authorization': 'Bearer ' + token_parsed}
    requestHeaders = {'Authorization': 'Bearer ' + token_parsed}

    page_append = 'pages?sectionName=Quick Notes'
    middle_url = 'v1.0/me/onenote/'
    full_url = graphURI + middle_url + 'notebooks'

    notebooks = msgraph_request(full_url,requestHeaders)

    #print(notebooks)

    #value = [{'id': '0-2170C8CE0F8F3556!82605', 'self': 'https://graph.microsoft.com/v1.0/users/acook999@gmail.com/onenote/sections/0-2170C8CE0F8F3556!82605', 'createdDateTime': '2022-10-31T22:45:19.533Z', 'displayName': 'Quick Notes', 'lastModifiedDateTime': '2022-11-15T03:08:41.49Z', 'isDefault': False, 'pagesUrl': 'https://graph.microsoft.com/v1.0/users/acook999@gmail.com/onenote/sections/0-2170C8CE0F8F3556!82605/pages', 'createdBy': {'user': {'id': '2170C8CE0F8F3556', 'displayName': 'Andrew Cook'}}, 'lastModifiedBy': {'user': {'id': '2170C8CE0F8F3556', 'displayName': 'Andrew Cook'}}, 'parentNotebook@odata.context': "https://graph.microsoft.com/v1.0/$metadata#users('acook999%40gmail.com')/onenote/sections('0-2170C8CE0F8F3556%2182605')/parentNotebook/$entity", 'parentNotebook': {'id': '0-2170C8CE0F8F3556!82603', 'displayName': "Andrew's Notebook", 'self': 'https://graph.microsoft.com/v1.0/users/acook999@gmail.com/onenote/notebooks/0-2170C8CE0F8F3556!82603'}, 'parentSectionGroup@odata.context': "https://graph.microsoft.com/v1.0/$metadata#users('acook999%40gmail.com')/onenote/sections('0-2170C8CE0F8F3556%2182605')/parentSectionGroup/$entity", 'parentSectionGroup': None}, {'id': '0-2170C8CE0F8F3556!82608', 'self': 'https://graph.microsoft.com/v1.0/users/acook999@gmail.com/onenote/sections/0-2170C8CE0F8F3556!82608', 'createdDateTime': '2022-10-31T22:45:41.247Z', 'displayName': 'Untitled Section', 'lastModifiedDateTime': '2022-10-31T22:45:43.1Z', 'isDefault': False, 'pagesUrl': 'https://graph.microsoft.com/v1.0/users/acook999@gmail.com/onenote/sections/0-2170C8CE0F8F3556!82608/pages', 'createdBy': {'user': {'id': '2170C8CE0F8F3556', 'displayName': 'Andrew Cook'}}, 'lastModifiedBy': {'user': {'id': '2170C8CE0F8F3556', 'displayName': 'Andrew Cook'}}, 'parentNotebook@odata.context': "https://graph.microsoft.com/v1.0/$metadata#users('acook999%40gmail.com')/onenote/sections('0-2170C8CE0F8F3556%2182608')/parentNotebook/$entity", 'parentNotebook': {'id': '0-2170C8CE0F8F3556!82603', 'displayName': "Andrew's Notebook", 'self': 'https://graph.microsoft.com/v1.0/users/acook999@gmail.com/onenote/notebooks/0-2170C8CE0F8F3556!82603'}, 'parentSectionGroup@odata.context': "https://graph.microsoft.com/v1.0/$metadata#users('acook999%40gmail.com')/onenote/sections('0-2170C8CE0F8F3556%2182608')/parentSectionGroup/$entity", 'parentSectionGroup': None}]

    notebooks_list = notebooks['value'] #some metadata in the notebooks json outside of value
    for notebook in notebooks_list:
        display_name = notebook['displayName']
        print(display_name)
        if display_name == "Andrew's Notebook":
            notebook_id = notebook['id']
            sections_url = graphURI + middle_url + 'notebooks/' + notebook_id + '/sections'
            sections = msgraph_request(sections_url,requestHeaders)
            #print(sections)
            sections_list = sections['value']
            for section in sections_list:
                section_name = section['displayName']
                print(section_name)
                section_id = section['id']

    # try:
    #     print(json.dumps(queryResults, indent=2))
    # except Exception as err:
    #     print(err)

    return 0

main()
exit()