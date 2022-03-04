import argparse
import zipfile
import re
from tokenfinder import Tokenfinder

def check_office_files():
    # Parsing arguments from master_script.py
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    parser.add_argument("--string", "-s", type=str, required=True)
    args = parser.parse_args()

    # Boolean to determine if anything is found
    found = 0
    try:
        # Unzip the office file without saving to folder
        unzipped_file = zipfile.ZipFile(args.file,"r")
        # List of all the content of the zip
        namelist = unzipped_file.namelist()
        # Reads every file in the zip file and looks if it contains the string you wish to search for
        for item in namelist:
            content = str(unzipped_file.read(item))
            tokenlist = re.findall(Tokenfinder.pattern, content)
            for token in tokenlist:
                for t in token:
                    if Tokenfinder.find_canarytoken(t):
                        print("Canarytoken found in: ", item)
                        print(t)
                        print()
                        found += 1
    except OSError:
        print("error")
    
    # If no results of the search
    if found == 0:
        print("No canarytoken found")

if __name__ == "__main__":
    check_office_files()
