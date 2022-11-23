#update the manifest (?) in azure to true values for "allow token" oauth2AllowIdTokenImplicitFlow
#use the url generated here to get token
#https://learn.microsoft.com/en-us/onedrive/developer/rest-api/getting-started/msa-oauth?view=odsp-graph-online
#redirect uri from here https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
#can't be localhost
#grab token from response url. Looks same at first, but it's different later in the token
#use that token in the header authorization: bearer token

import PASS

def main():

    client_id = PASS.personal_client_id #app client id. app must be for personal accounts
    scope = ['Notes.Read.All','Notes.ReadWrite.All','User.Read','Notes.ReadWrite','Notes.Read','Notes.Create']
    scopeStr = ' '.join(scope)
    redirect_uri = PASS.redirect_uri #probably https://login.microsoftonline.com/common/oauth2/nativeclient

    get_url = 'https://login.live.com/oauth20_authorize.srf?client_id='+client_id+'&scope='+scopeStr+'&response_type=token&redirect_uri='+redirect_uri

    print(get_url)

    #can't do anything programatically - have to go into browser and click "allow" to get key

main()
exit()