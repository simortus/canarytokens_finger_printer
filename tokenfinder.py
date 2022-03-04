import re
class Tokenfinder():
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»""'']))"
    pattern = re.compile(regex)
    # The 'find_canarytoken' function is made by thinkst as part of Canarytokens.
    # The source code can be found at https://github.com/thinkst/canarytokens
    # Their licens for the code can be found at https://github.com/thinkst/canarytokens/blob/master/LICENSE
    def find_canarytoken(haystack):

        canarytoken_ALPHABET=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3',
                    '4', '5', '6', '7', '8', '9']
        canarytoken_LENGTH=25 # equivalent to 128-bit id
        CANARY_RE = re.compile('.*(['+''.join(canarytoken_ALPHABET)+']{'+
                          str(canarytoken_LENGTH)+'}).*', re.IGNORECASE)



        m = CANARY_RE.match(haystack)
        if not m:
            return None

        return m.group(1)
