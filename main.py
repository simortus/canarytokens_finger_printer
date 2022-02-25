import base64
import subprocess
import platform as pt

wind_commands = ["certutil -encode"]
mac_lin_commands = ["base64"]


#     os_name = os_name()
#     if "Mac" in os_name or "Linux" in os_name:
#         b64(mac_lin_commands[0])
#     elif "Windows" in os_name:
#         b64(mac_lin_commands[0])

# file_input = open("wireguard-conf-hk","r") #open file
# file_data = file_input.read() #read file data
# message = file_data.encode('ascii')
# b64 = str(base64.b64encode(message))
# print(b64)


def os_name():
    return pt.platform()


def ip_address():
    # this nslookup is generic to all the platform, so we simply use one.
    p = subprocess.Popen(["nslookup", "canarytokens.org"], stdout=subprocess.PIPE)
    out, err = p.communicate()
    result = out.decode("utf-8")
    final = result.split("Address:")
    ip = final[2].strip()
    return ip


# decide on wheter to use this in one function
def b64(file_location):
    p = subprocess.Popen(["base64", file_location], stdout=subprocess.PIPE)
    out, err = p.communicate()
    result1 = out.decode("utf-8")
    return result1


def find_honey_token(file_location):
    ip = ip_address()
    print(ip)

    file_encoded = b64(file_location)
    print(file_encoded)

    ip_encoded = str(base64.b64encode(ip.encode('ascii'))).replace("=", "")
    print(ip_encoded)

    if file_encoded.find(ip_encoded):
        print("GOTCHA! Honey token found")
        subprocess.run(["say", "Honey-token found"])


if __name__ == "__main__":
    val = input("Enter filename or full-path: ")
    find_honey_token(val)
