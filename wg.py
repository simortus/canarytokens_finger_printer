# import argparse
# import socket
#
# # add other domains here for reverse dns
# domains = ["www.canarytokens.org"]
#
#
# def check_file(file):
#     content = open(file).read().split()  # read file and split it to obtain a list
#     temp = ""
#
#     for i in range(len(content)):
#         if content[i].__contains__("Endpoint"):
#             temp += content[i + 2]
#     ip = temp.split(":")[0]
#     print(ip)
#     domain_ip = reverse_dns()
#     if domain_ip is not None and domain_ip == ip:
#         print("<----!!!!----> Honey-Token found <----!!!!---->")
#     else:
#         print("Nothing found")
#
#
#
# def main():
#     print("-------- START WIREGUARD.PY --------")
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--file", "-f", type=str, required=True)
#     args = parser.parse_args()
#     file = args.file
#     check_file(file)
#
#
# def reverse_dns():
#     return socket.gethostbyname(domains[0])
#
#
# # /Users/mm/Desktop/canary-tokens/wg
# if __name__ == "__main__":
#     main()
