OKAY so I made this to switch to Onenote as my primary note app instead of evernote. I wanted to to archive my old evernote notes that I barely look at anyway but didn't want to lose. I wasn't too worried about keeping formatting or images. I was able to pull the evernote content as-is and throw it into onenote and that was good enough for me. If you want something super robust this might not work. All i wanted to do was keep a decent running archive of my old notes before switching to using Onenote full time.

I made it so that each of my Evernote notebooks became a SECTION in Onenote. Which made sense to me. Then notes are added in reverse chronological order so that the last modified notes appear at the top.

Steps:
1. Download the repo
2. Rename PASS_TEMPLATE.py to PASS.py. This file will be used for your credentials
3. Open evernote.com and log in 
4. Go to cookies in your browser (dev tools). Find the "auth" cookie. Copy the value and set it as your evernote_token in PASS.py
5. Set up your Azure account correctly and make an app to work with apis
    
    Okay this took me a while to figure out. Make an Azure account. Make an app. Make sure it's personal. You might have to mess with the manifest. check some of the urls in access_token_url.py. If you really want to use this make an issue in github and I'll try to help
6. Set personal_client_id to your azure app client id and redirect_uri as appropriate (see default in access_token_url.py)
7. Run access_token_url.py
8. Take the output in put it in your web browser. Go to that url. You might have to accept permissions here
9. Copy the new url that shows up (the access token you need is buried in there) and set full_token variable in pass.py to that url
10. Run evernote_to_onenote.py. you might get limited by api calls. I made an array in the script to be able to specify notebooks that are already done exporting. Use that so you don't have to start completely over