import argparse
import string
import re
from tokenfinder import Tokenfinder
# The sql dump can either contain the domain canarytokens.com in plain text or encoded in base64
# This function will check every line and look for 'canary'. 
# It also tries to decode every line in case the line is base64 encoded
def find_canary(file_location):
    file = open(file_location, 'r')
    lines = file.readlines()

    # List for URLs found
    list_of_urls = []
    
    for line in lines:
    # Checks the line to see if canary is written in plain text
        token = Tokenfinder.find_tokens_in_string(line)
        if token:
            list_of_urls.append(token)

    # If no results of the search
    if len(list_of_urls) == 0:
        print("No canaries detected")
        return None
    else:
        print(str(len(list_of_urls)) +" canary URLs detected in the file")
        for url in list_of_urls:
            print("Canary detected: ", url)
            print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    args = parser.parse_args()
    
    file_location = args.file

    find_canary(file_location)