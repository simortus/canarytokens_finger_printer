import re
import zlib
import argparse
from tokenfinder import Tokenfinder

def find_token_in_pdf(file_location):

    # List for URLs found
    list_of_urls = []


    pdf = open(file_location, "rb").read()
    stream = re.compile(b'.*?FlateDecode.*?stream(.*?)endstream', re.S)

    for s in re.findall(stream,pdf):
        s = s.strip(b'\r\n')
        line = ""
        try:
            line = zlib.decompress(s).decode('UTF-8')
            print(line)
        except:
            pass
        token = Tokenfinder.find_tokens_in_string(line)
        if token:
            list_of_urls.extend(token)
    
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

    find_token_in_pdf(file_location)
