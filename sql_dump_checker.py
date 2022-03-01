import re
import string
import base64
import sys

# The sql dump can either contain the domain canarytokens.com in plain text or encoded in base64
# This function will check every line and look for 'canary'. 
# It also tries to decode every line in case the line is base64 encoded
def sql_dump_checker(file_location, string_to_search):
    file = open(file_location, 'r')
    lines = file.readlines()

    for line in lines:
    # Checks the line to see if canary is written in plain text
        if "canary" in line:
            print("Canary detected:")
            print(line)

        # Regex for characers found in base64
        pattern = re.compile('[^a-zA-Z0-9+=]')
        alnum = pattern.sub('',line)
        
        # Tries to decode the line, to see if the line is base64 encoded
        try:
            decoded = str(base64.b64decode(alnum))
            if string_to_search in decoded:
                print("Canary detected:")
                print(decoded)
        except:
            continue

if __name__ == "__main__":
    file_location = sys.argv[2]
    if len(sys.argv) != 5:
        print("Please enter string to search")
        exit(1)
    string_to_search = sys.argv[4]
    sql_dump_checker(file_location, string_to_search)