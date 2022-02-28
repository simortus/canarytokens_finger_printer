from os import path
import os
import argparse
import zipfile


def main():
    print("-------- START DOCX.PY --------")
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    parser.add_argument("--string", "-s", type=str, required=True)
    args = parser.parse_args()
    print(args.string)
    try:
        if path.exists(args.file):
            orgf = args.file
            os.rename(args.file, 'temp.zip')
            with zipfile.ZipFile('temp.zip', 'r') as zip_ref:
                zip_ref.extractall("temp")
                tokenfile = os.path.join(os.getcwd(), "temp/word/footer2.xml")
                print(tokenfile)
            with open(tokenfile) as f:
                if args.string in f.read():
                    print("Canarytoken detected")
                else:
                    print("Not a honeytoken.")
            os.rename("temp.zip", orgf)
    except OSError:
        print("error")

if __name__ == "__main__":
    main()
