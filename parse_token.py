#found myself using this a lot in testing so moved to its own file
import re

def parse_token(full_token):
    p = re.search('=(.*?)&', full_token) #regex for between = and &. re.search gets the values between
    return p.group(1)