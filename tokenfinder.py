import re
import urllib
class Tokenfinder():
    # The 'find_canarytoken' function is made by thinkst as part of Canarytokens and then slightly modified by us.
    # The source code can be found at https://github.com/thinkst/canarytokens
    # Their licens for the code can be found at https://github.com/thinkst/canarytokens/blob/master/LICENSE


    def __find_canarytoken(string):
        canarytoken_ALPHABET=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3',
                    '4', '5', '6', '7', '8', '9']
        canarytoken_LENGTH=25 # equivalent to 128-bit id
        CANARY_RE = re.compile('.*(['+''.join(canarytoken_ALPHABET)+']{'+
                          str(canarytoken_LENGTH)+'}).*', re.IGNORECASE)
        # Regex for splitting url
        regex = r"([.]|/|[@])"
        #Split url into array
        array = re.split(regex, string)
        #For every index of the array, check if the string is exactly 25 chars
        for s in array:
            if len(s) == 25:
                # See if the 25 char string is in the canarytoken alphabet
                m = CANARY_RE.match(string)
                if not m:
                    return None
                return True

    def find_tokens_in_string(string):
        
        #Regex for finding domains, subdomains and ip adresses
        regex = r"\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b"
        pattern = re.compile(regex, re.MULTILINE)
        
        # Array of urls
        list_of_urls = []

        # Find all domains, subdomains and ip addresses
        tokenlist = re.findall(pattern, string)
        # Check every entry in the list
        for token in tokenlist:
            #Call to see if the entry(the url) is a canarytoken
            if Tokenfinder.__find_canarytoken(token):
                list_of_urls.append(token)
        
        #Regex for finding emails
        regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        pattern = re.compile(regex, re.MULTILINE)
        # Find all email addresses
        tokenlist = re.findall(pattern, string)
        # Check every entry in the list
        for token in tokenlist:
            #Call to see if the entry(the url) is a canarytoken
            if Tokenfinder.__find_canarytoken(token):
                list_of_urls.append(token)

                
        return list_of_urls
        