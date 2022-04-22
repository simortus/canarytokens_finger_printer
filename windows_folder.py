import argparse
import re
from tokenfinder import Tokenfinder


def check_ini_file(file):
    list_of_urls = []
    with open(file, encoding="utf-16") as f:
        for line in f:
            print(line)
            token = Tokenfinder.find_tokens_in_string(line)
            if token:
                list_of_urls.extend(token)
    
    if len(list_of_urls) == 0:
        return None
    else:
        print(str(len(list_of_urls)) +" canary URLs detected in the file")
    for entry in list_of_urls:
        print(entry)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    args = parser.parse_args()
    check_ini_file(args.file)


if __name__ == "__main__":
    main()