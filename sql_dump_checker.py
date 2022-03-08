import argparse
import string
import base64
import re
from tokenfinder import Tokenfinder
# The sql dump can either contain the domain canarytokens.com in plain text or encoded in base64
# This function will check every line and look for 'canary'. 
# It also tries to decode every line in case the line is base64 encoded
def sql_dump_checker(file_location):
    file = open(file_location, 'r')
    lines = file.readlines()
   
    # Boolean to see if anything is found
    found = 0

    # List for URLs found
    list_of_url = []
    
    for line in lines:
    # Checks the line to see if canary is written in plain text
        token = Tokenfinder.find_tokens_in_string(line)
        if token:
            list_of_url.append(token)
            found += 1

        # Regex for characers found in base64
        pattern = re.compile('[^a-zA-Z0-9+=]')
        alnum = pattern.sub('',line)
        
        # Tries to decode the line, to see if the line is base64 encoded
        try:
            decoded = str(base64.b64decode(alnum))
            token = Tokenfinder.find_tokens_in_string(decoded)
            if token:
                list_of_url.append(token)
                found += 1
        except:
            continue

    # If nothing is found
    if found == 0:
        print("None")
        return None
    else:
        print(list_of_url)
        return list_of_url

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    args = parser.parse_args()
    
    file_location = args.file

    sql_dump_checker(file_location)