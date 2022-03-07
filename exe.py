import argparse


def check_file(filename):
    # read file and split it to obtain a list
    global content
    try:
        file = open(filename, "r+b")
        content = str(file.read())
    except Exception as e:
        print(f"Exception: {e}")
    if content.__contains__("canary"):
        print("<----!!!!----> Honey-Token found <----!!!!---->")
    else:
        print("Nothing found")


def main():
    print("-------- START EXE.PY --------")
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    args = parser.parse_args()
    filename = args.file
    check_file(filename)


# /Users/mm/Desktop/canary-tokens/exe.exe
if __name__ == "__main__":
    main()
