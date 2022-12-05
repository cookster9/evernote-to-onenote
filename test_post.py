import requests
from datetime import datetime

import re

import PASS
def parse_token(full_token):
    p = re.search('=(.*?)&', full_token) #regex for between = and &. re.search gets the values between
    return p.group(1)

def main():
    full_token_url = PASS.token_current #the entire url that shows up after navigating to the url generated by access_token_url
    token_parsed = parse_token(full_token_url)
    requestHeaders = {'Authorization': 'Bearer ' + token_parsed, 'Content-Type': 'text/html'}
    # requestHeaders = {'Authorization': token_parsed}

    # #open text file in read mode
    # text_file = open(".\IGNORE_evernote_note.txt", "r")
    
    # #read whole file to a string
    # data = text_file.read()
    header_data0 = '''<!DOCTYPE html>
                <html>
                <head>
                    <title>
            '''
    header_data1 = '''</title>
            <meta name="created" content="
            '''
    note_data = '''" />
            </head>
            <en-note><div>Paint</div><div>Ben moore has lighting guide:</div><div><a href="https://www.benjaminmoore.com/en-us/color-overview/color-palettes/color-by-direction/west-facing-room-paint-colors" rev="en_rl_none">https://www.benjaminmoore.com/en-us/color-overview/color-palettes/color-by-direction/west-facing-room-paint-colors</a></div><div><br /></div><div>living room:</div><div style="padding-left:40px;">Grey:</div><div style="padding-left:40px;">Moonshine:</div><div style="padding-left:40px;"><a href="https://westmagnoliacharm.com/benjamin-moore-moonshine-oc-56/painting/" rev="en_rl_none">https://westmagnoliacharm.com/benjamin-moore-moonshine-oc-56/painting/</a></div><div style="padding-left:40px;">Might clash with couch? Would need pillows and color</div><div style="padding-left:80px;">Inspo post has a grey chair</div><div style="padding-left:80px;">Do bedroom</div><div style="padding-left:80px;">Or anything that can do blue do bedroom</div><div style="padding-left:40px;"><a href="https://www.benjaminmoore.com/en-us/paint-colors/color/af-690/metropolitan" rev="en_rl_none">https://www.benjaminmoore.com/en-us/paint-colors/color/af-690/metropolitan</a></div><div style="padding-left:80px;">"versatile"</div><div style="padding-left:40px;"><br /></div><div style="padding-left:40px;">White:</div><div style="padding-left:40px;">Could go white everywhere:</div><div style="padding-left:40px;"><a href="https://www.benjaminmoore.com/en-us/paint-colors/color/oc-17/white-dove" rev="en_rl_none">https://www.benjaminmoore.com/en-us/paint-colors/color/oc-17/white-dove</a></div><div style="padding-left:80px;">"versatile". warm enough for lower light?</div><div style="padding-left:80px;"><a href="https://www.acehardware.com/benjamin-moore-ben-eggshell-base-1-paint-and-primer-interior-1-gal/p/1020315?code=oc-17">https://www.acehardware.com/benjamin-moore-ben-eggshell-base-1-paint-and-primer-interior-1-gal/p/1020315?code=oc-17</a></div><div style="padding-left:80px;"><br /></div><div style="padding-left:40px;"><a href="https://www.benjaminmoore.com/en-us/paint-colors/color/oc-54/white-wisp" rev="en_rl_none">https://www.benjaminmoore.com/en-us/paint-colors/color/oc-54/white-wisp</a></div><div style="padding-left:80px;">blue toned. good with grey</div><div style="padding-left:40px;"><a href="https://www.benjaminmoore.com/en-us/paint-colors/color/oc-22/calm" rev="en_rl_none">https://www.benjaminmoore.com/en-us/paint-colors/color/oc-22/calm</a></div><div style="padding-left:80px;">mom recommended. matches fun blue for front door</div><div style="padding-left:40px;"><a href="https://www.benjaminmoore.com/en-us/paint-colors/color/oc-57/white-heron" rev="en_rl_none">https://www.benjaminmoore.com/en-us/paint-colors/color/oc-57/white-heron</a></div><div style="padding-left:80px;">The other one</div><div style="padding-left:40px;"><br /></div><div style="padding-left:40px;"><br /></div><div style="padding-left:40px;">Neutral:</div><div style="padding-left:40px;">Pewter:</div><div style="padding-left:40px;">Would work with grey couch actually</div><div style="padding-left:40px;"><a href="https://www.benjaminmoore.com/en-us/paint-colors/color/hc-172/revere-pewter" rev="en_rl_none">https://www.benjaminmoore.com/en-us/paint-colors/color/hc-172/revere-pewter</a></div><div style="padding-left:40px;">Would also work better in kitchen maybe for both</div><div style="padding-left:80px;">Do everything this</div><div style="padding-left:40px;">Ashwood:</div><div style="padding-left:40px;"><a href="https://www.benjaminmoore.com/en-us/paint-colors/color/oc-47/ashwood" rev="en_rl_none">https://www.benjaminmoore.com/en-us/paint-colors/color/oc-47/ashwood</a></div><div style="padding-left:80px;">Has more interesting complimentary colors</div><div style="padding-left:80px;">lightest beige</div><div style="padding-left:40px;"><br /></div><div><br /></div><div>kitchen:</div><div style="padding-left:40px;"><a href="https://www.benjaminmoore.com/en-us/paint-colors/color/oc-121/mountain-peak-white" rev="en_rl_none">https://www.benjaminmoore.com/en-us/paint-colors/color/oc-121/mountain-peak-white</a></div><div style="padding-left:40px;">White for kitchen</div><div style="padding-left:40px;">or just go super white:</div><div style="padding-left:40px;"><a href="https://www.benjaminmoore.com/en-us/paint-colors/color/oc-117/simply-white" rev="en_rl_none">https://www.benjaminmoore.com/en-us/paint-colors/color/oc-117/simply-white</a></div><div style="padding-left:40px;"><br /></div><div style="padding-left:40px;">accent wall around corner?</div><div><br /></div><div><br /></div><div>Front door:</div><div style="padding-left:40px;">Slate blue:</div><div style="padding-left:40px;"><a href="https://www.benjaminmoore.com/en-us/paint-colors/color/1648/slate-blue" rev="en_rl_none">https://www.benjaminmoore.com/en-us/paint-colors/color/1648/slate-blue</a></div><div style="padding-left:40px;">Matches greys</div><div style="padding-left:80px;">THIS</div><div style="padding-left:40px;"><br /></div><div style="padding-left:40px;">Silvery blue:</div><div style="padding-left:40px;"><a href="https://www.benjaminmoore.com/en-us/paint-colors/color/1647/silvery-blue" rev="en_rl_none">https://www.benjaminmoore.com/en-us/paint-colors/color/1647/silvery-blue</a></div><div style="padding-left:40px;">lighter, also matches greys</div><div style="padding-left:80px;">Maybe better for west facing?</div><div style="padding-left:80px;"><br /></div><div style="padding-left:40px;"><a href="https://www.benjaminmoore.com/en-us/paint-colors/color/hc-155/newburyport-blue" rev="en_rl_none">https://www.benjaminmoore.com/en-us/paint-colors/color/hc-155/newburyport-blue</a></div><div style="padding-left:80px;">would maybe match inside more. plus the above two are pretty light</div><div style="padding-left:120px;">matches "calm"</div><div><br /></div><div>Office:</div><div style="padding-left:40px;">Don't love the green tbh</div><div style="padding-left:40px;"><a href="https://www.benjaminmoore.com/en-us/paint-colors/color/oc-10/white-sand" rev="en_rl_none">https://www.benjaminmoore.com/en-us/paint-colors/color/oc-10/white-sand</a></div><div style="padding-left:40px;">Nice beige</div><div style="padding-left:40px;">Caldwell green for door:</div><div style="padding-left:40px;"><a href="https://www.benjaminmoore.com/en-us/paint-colors/color/hc-124/caldwell-green" rev="en_rl_none">https://www.benjaminmoore.com/en-us/paint-colors/color/hc-124/caldwell-green</a></div><div style="padding-left:40px;"><br /></div><div style="padding-left:40px;"><a href="https://www.benjaminmoore.com/en-us/paint-colors/color/af-95/hush" rev="en_rl_none">https://www.benjaminmoore.com/en-us/paint-colors/color/af-95/hush</a></div><div style="padding-left:80px;">This if we’re calling it south facing</div><div style="padding-left:40px;"><br /></div><div style="padding-left:40px;"><a href=
            "https://www.benjaminmoore.com/en-us/paint-colors/color/hc-147/woodlawn-blue" rev="en_rl_none">https://www.benjaminmoore.com/en-us/paint-colors/color/hc-147/woodlawn-blue</a></div><div style="padding-left:80px;">lighter blue green. should be fun?</div><div style="padding-left:120px;">red for door maybe:</div><div 
            style="padding-left:160px;"><a href="https://www.benjaminmoore.com/en-us/paint-colors/color/1281/tawny-port" rev="en_rl_none">https://www.benjaminmoore.com/en-us/paint-colors/color/1281/tawny-port</a></div><div><br /></div><div>Bedroom:</div><div style="padding-left:40px;"><a href="https://www.benjaminmoore.com/en-us/paint-colors/color/af-540/constellation" rev="en_rl_none">https://www.benjaminmoore.com/en-us/paint-colors/color/af-540/constellation</a></div><div style="padding-left:80px;">Nice blue, "popular" for bedrooms</div><div style="padding-left:40px;">Moonshine, original thought:</div><div style="padding-left:80px;"><a href="https://westmagnoliacharm.com/benjamin-moore-moonshine-oc-56/painting/" rev="en_rl_none">https://westmagnoliacharm.com/benjamin-moore-moonshine-oc-56/painting/</a></div><div style="padding-left:40px;">Other blue that i have, try it:</div><div style="padding-left:80px;"><a href="https://www.benjaminmoore.com/en-ca/paint-colours/colour/hc-147/woodlawn-blue" rev="en_rl_none">https://www.benjaminmoore.com/en-ca/paint-colours/colour/hc-147/woodlawn-blue</a></div><div><br /></div><div>Measure rooms</div><div>get some samples?</div><div>See what the color is for the brick 
            paint</div>
            </en-note>
            </html>
            '''
    #print(data)
    
    #pages get posted in order down. So you start posting to a section id, pages will display like:
    #first
    #second
    #third
    #etc
    title = "7/11/22"
    date = "2022-07-14 15:23:06"
    for i in range(1):
        section_id = PASS.test_section
        url = 'https://graph.microsoft.com/v1.0/me/onenote/sections/'+section_id+'/pages'

        note_data = re.sub('[’]', '', note_data)

        data = header_data0 + title + header_data1 + date + note_data
        #have to parse out characters as well: ’

        results = requests.post(url, data, headers=requestHeaders)  #get(resource, headers=requestHeaders).json()
        print(results.json())
        # text_file.close()

main()
exit()