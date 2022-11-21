import msal
import jwt
import json
import sys
import requests
from datetime import datetime

import re

import PASS

accessToken = None 
requestHeaders = None 
tokenExpiry = None 
queryResults = None 
graphURI = 'https://graph.microsoft.com'
tenantID = PASS.tenant_id
authority = 'https://login.microsoftonline.com/' + tenantID 
authority = 'https://login.microsoftonline.com/common/oauth2/token'
clientID = PASS.personal_client_id
clientSecret = PASS.msal_secret
scope = ['https://graph.microsoft.com/.default']

queryUser = PASS.user_name
user_id = PASS.user_id

def msal_public_auth(clientID, scope, authority):      
    # app = msal.ConfidentialClientApplication(clientID, authority=authority, client_credential=clientSecret)
    app = msal.PublicClientApplication(clientID, authority=authority)
    result = app.acquire_token_interactive(scopes=scope)
    print(result)
    return result 

def msgraph_request(resource, requestHeaders):
    # Request
    results = requests.get(resource, headers=requestHeaders).json()
    return results

def msgraph_post(resource, requestHeaders):
    # Request
    results = requests.post(resource, headers=requestHeaders)
    return results

def msal_jwt_expiry(accessToken): 
    alg = jwt.get_unverified_header(accessToken['access_token'])['alg']
    decodedAccessToken = jwt.decode(accessToken['access_token'], algorithms=[alg], options={"verify_signature": False})
    accessTokenFormatted = json.dumps(decodedAccessToken, indent=2) 

    # Token Expiry 
    tokenExpiry = datetime.fromtimestamp(int(decodedAccessToken['exp'])) 
    print("Token Expires at: " + str(tokenExpiry)) 
    return tokenExpiry 

def parse_token(full_token):
    print(full_token)
    p = re.search('=(.*?)&', full_token)
    print(p)
    return p.group(1)

# Auth
try:
    full_token_url = PASS.token_current
    token_parsed = parse_token(full_token_url)
    accessToken = {'Authorization': 'Bearer ' + token_parsed}
    requestHeaders = {'Authorization': 'Bearer ' + token_parsed}
    if not accessToken:
        try:
            # Get a new Access Token using Client Credentials Flow and a Self Signed Certificate
            accessToken = msal_public_auth(clientID, scope, authority)
            requestHeaders = {
                'Authorization': 'Bearer ' + accessToken['access_token']}
        except Exception as err:
            print('Error acquiring authorization token. Check your tenantID, clientID and certficate thumbprint.')
            print(err)
    if accessToken and False:
        # Example of checking token expiry time to expire in the next 10 minutes
        alg = jwt.get_unverified_header(accessToken['access_token'])['alg']
        decodedAccessToken = jwt.decode(accessToken['access_token'], algorithms=[alg], options={"verify_signature": False})
        accessTokenFormatted = json.dumps(decodedAccessToken, indent=2)
        print("Decoded Access Token")
        print(accessTokenFormatted)

        # Token Expiry
        tokenExpiry = datetime.utcfromtimestamp(decodedAccessToken["exp"])
        print('Token Expiry: ' + str(tokenExpiry))
        now = datetime.utcnow()
        time_to_expiry = tokenExpiry - now

        if time_to_expiry.seconds < 600:
            print("Access Token Expiring Soon. Renewing Access Token.")
            accessToken = msal_certificate_auth(clientID, scope, authority, thumbprint, certfile)
            requestHeaders = {'Authorization': 'Bearer ' + accessToken['access_token']}
        else:
            minutesToExpiry = time_to_expiry.seconds / 60
            print("Access Token Expires in '" + str(minutesToExpiry) +" minutes'")

except Exception as err:
    print(err)

# Query

if requestHeaders and accessToken:
    # full_url = graphURI + '/v1.0/users/'+user_id+'/onenote/notebooks'
    

    page_append = '/pages?sectionName=Quick Notes'
    full_url = graphURI + '/v1.0/me/onenote' + page_append

    print(full_url)
    print(requestHeaders)
    # queryResults = msgraph_request(full_url,requestHeaders)
    postResults = msgraph_post(full_url,requestHeaders)
    try:
        print(json.dumps(queryResults, indent=2))
    except Exception as err:
        print(err)