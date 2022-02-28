import re
import string
import base64


def sql_dump_checker(file_location):
    file = open(file_location, 'r')
    lines = file.readlines()

    for line in lines:
        pattern = re.compile('[^a-zA-Z0-9+=]')
        alnum = pattern.sub('',line)     
        try:
            decoded = str(base64.b64decode(alnum))
            if "canary" in decoded:
                print("Canary detected:")
                print(decoded)
        except:
            continue

if __name__ == "__main__":
    file_location = input("FIle Path:\n")
    sql_dump_checker(file_location)