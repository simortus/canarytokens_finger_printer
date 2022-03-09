import os
import re
import string
import argparse
from tokenfinder import Tokenfinder


def strings(filename, min=4):  # gets all strings of printable character in the given file with characters >=4
    with open(filename, errors="ignore") as f:
        result = ""
        for c in f.read():
            if c in string.printable:
                result += c
                continue
            if len(result) >= min:
                yield result
            result = ""
        if len(result) >= min:  # catch result at EOF
            yield result


if __name__ == "__main__":
    print("-------- START EXE.PY --------")
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    args = parser.parse_args()
    filename = args.file
    for s in strings(filename):
        # calls the find_tokens_in_string() function and checks the strings for a pattern in any url found
        result = Tokenfinder.find_tokens_in_string(s)
        if len(result) > 0:
            print("Honeytoken detected")
            print(result)

