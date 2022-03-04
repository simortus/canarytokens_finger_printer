import argparse
import zipfile
import re
from tokenfinder import Tokenfinder

def check_office_files(file_location):
    # Parsing arguments from master_script.py
    
    parser.add_argument("--string", "-s", type=str, required=True)
    

    # List of urls found
    list_of_urls = []
    try:
        # Unzip the office file without saving to folder
        unzipped_file = zipfile.ZipFile(args.file,"r")
        # List of all the content of the zip
        namelist = unzipped_file.namelist()
        # Reads every file in the zip file and looks if it contains the string you wish to search for
        for item in namelist:
            content = str(unzipped_file.read(item))
            token = Tokenfinder.find_tokens_in_string(content)
            if token:
                list_of_urls.extend(token)
    except OSError:
        print("error")
    
    # If no results of the search
    if len(list_of_urls) == 0:
        return None
    else:
        print(list_of_urls)
        return list_of_urls

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    args = parser.parse_args()
    
    file_location = args.file

    check_office_files(file_location)