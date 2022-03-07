import argparse
import socket
from tokenfinder import Tokenfinder

# add other domains here for reverse dns
domains = ["www.canarytokens.org"]


def reverse_dns():
    return socket.gethostbyname(domains[0])


def check_file(filename):
    content_aslist = open(filename).read().split()  # read file and split it to obtain a list
    temp = ""
    ip = ""
    for i in range(len(content_aslist)):
        if content_aslist[i].__contains__("server"):  # kubernetes-conf has 'server' entry for the backend-server ip
            temp += content_aslist[i + 1]
            ip = temp.split("//")[1].split(":")[0]  # split and strip from extras >> https : // : port 
        elif content_aslist[i].__contains__(
                "Endpoint"):  # wireguard-conf has 'endpoint' entry for the backend-server ip
            temp += content_aslist[i + 2]
            ip = temp.split(":")[0]  # split and strip from extras >> https : // : port 
    domain_ip = reverse_dns()  # reverse dns lookup of a domain name to compare the ip with the one found in the file
    if domain_ip is not None and domain_ip == ip:
        print("Canary-Token detected !!!")
    else:
        print("Nothing found.")


def main():
    print("-------- START CONF.PY --------")
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    args = parser.parse_args()
    filename = args.file
    check_file(filename)


# /Users/mm/Desktop/canary-tokens/exe.exe
if __name__ == "__main__":
    main()
