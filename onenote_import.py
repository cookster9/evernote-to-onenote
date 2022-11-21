#onenote import
from azure.identity import AzureCliCredential
from azure.identity import DefaultAzureCredential
from azure.identity import EnvironmentCredential
from azure.identity import InteractiveBrowserCredential
from msgraph.core import GraphClient
from azure.identity import ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient
from azure.identity import UsernamePasswordCredential

import msal

import requests 
import PASS
import json

import pandas as pd

accessToken = None 
requestHeaders = None 
tokenExpiry = None 
queryResults = None 
graphURI = 'https://graph.microsoft.com'

def main():
    global accessToken
    global requestHeaders
    global tokenExpiry

    tenant_id = PASS.tenant_id
    authority="https://login.microsoftonline.com/"+tenant_id

    client_id = PASS.personal_client_id
    client_secret = PASS.msal_secret
    scope = ['Notes.Read.All','Notes.ReadWrite.All','User.Read','Notes.ReadWrite','Notes.Read','Notes.Create']
    scopeStr = ' '.join(scope)
    redirect_uri = PASS.redirect_uri

    get_url = 'https://login.live.com/oauth20_authorize.srf?client_id='+client_id+'&scope='+scopeStr+'&response_type=token&redirect_uri='+redirect_uri

    #update the manifest (?) in azure to true values for "allow token" oauth2AllowIdTokenImplicitFlow
    #use this url to get token
    #https://learn.microsoft.com/en-us/onedrive/developer/rest-api/getting-started/msa-oauth?view=odsp-graph-online
    #redirect uri from here https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
    #can't be localhost
    #grab token from response url. Looks same at first, but it's different later in the token
    #use that token in the header authorization: bearer token

    # get_url = 'https://login.microsoftonline.com/0db307f7-9310-49bc-896b-a74b515ad034/oauth2/v2.0/token'
    print(get_url)

    #can't do anything programatically - have to go into browser and click "allow" to get key

main()
exit()