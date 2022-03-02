import argparse
import base64
import socket

# add other domains here for reverse dns
domains = ["www.canarytokens.org"]


def check_file(file, keyword):
    content = open(file).read().split()  # read file and split it to obtain a list
    temp = ""
    # loop through the list to find the endpoint entry. if yes, the ip is at index+2
    for i in range(len(content)):
        if content[i].__contains__("server"):
            temp += content[i + 1]
    ip = temp.split("//")[1].split(":")[0]  # split the string gives us a list of element [ip, port]. we chose index 0
    domain_ip = reverse_dns(keyword)

    if domain_ip is not None and reverse_dns(keyword) == ip:
        print("<----!!!!----> Honey-Token found <----!!!!---->")
    else:
        print("Nothing found")


def main():
    print("-------- START WIREGUARD.PY --------")
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    parser.add_argument("--string", "-s", type=str, required=True)
    args = parser.parse_args()
    print(args.string)
    file = args.file
    keyword = args.string
    check_file(file, keyword)


def reverse_dns(keyword):
    for i in range(len(domains)):
        if domains[i].__contains__(keyword):
            return socket.gethostbyname(domains[i])
        else:
            return None


# /Users/mm/Desktop/canary-tokens/wireguard-conf-hk
if __name__ == "__main__":
    main()
