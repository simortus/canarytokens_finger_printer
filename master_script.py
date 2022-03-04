import os
import subprocess


def get_type(file):
    print("-------- GET TYPE  --------")
    file_name, file_extension = os.path.splitext(file)
    print(f"Filename: {file_name}")
    print(f"File extension: {file_extension}")
    return file_extension


def is_kubeconfig_file(file):
    kubeconf_keywords = ["apiVersion", "kind", "clusters",
                         "users", "contexts", "current-context"]
    file_content = open(file).read()
    if file_content.__contains__(kubeconf_keywords[0]) \
            and file_content.__contains__(kubeconf_keywords[1]) \
            and file_content.__contains__(kubeconf_keywords[2]) \
            and file_content.__contains__(kubeconf_keywords[3]) \
            and file_content.__contains__(kubeconf_keywords[4]) \
            and file_content.__contains__(kubeconf_keywords[5]):
        return True


def is_wireguard_file(file):
    wireguard_keywords = ["[Interface]", "PrivateKey", "Address",
                          "[Peer]", "PublicKey", "AllowedIPs", "Endpoint", "PersistentKeepalive"]
    file_content = open(file).read()
    if file_content.__contains__(wireguard_keywords[0]) \
            and file_content.__contains__(wireguard_keywords[1]) \
            and file_content.__contains__(wireguard_keywords[2]) \
            and file_content.__contains__(wireguard_keywords[3]) \
            and file_content.__contains__(wireguard_keywords[4]) \
            and file_content.__contains__(wireguard_keywords[5]) \
            and file_content.__contains__(wireguard_keywords[6]) \
            and file_content.__contains__(wireguard_keywords[7]):
        print("This is a Wireguard config file")
        return True


def run_process(file, script):
    p = subprocess.run(["python %s -f %s" % (script, file)], stdout=True, shell=True)


def main():
    print("-------- START SCRIPT  --------")
    file = input("Enter filename or full path: ")
    if not os.path.exists(file):
        print("File not found. Check the path.")
        return (1)

    type = get_type(file)
    print("-------- CASE  --------")

    if ".txt" in type:
        print("Text file found.")

    elif ".pdf" in type:
        print("Pdf file found.")

    elif ".xlsx" in type:
        print("Excel file found.")

    elif ".docx" in type:
        print("Word document found.")
        run_process(file, "office_docx.py")

    elif ".sql" in type:
        print("SQL file found.")

    elif ".conf" in type:
        print("Configuration file found.")

    elif "_" in type or "" in type:
        print("No file extension.")
        if is_wireguard_file(file):
            run_process(file, "wg.py")
        if is_kubeconfig_file(file):
            print("Kubernetes config file detected")
            run_process(file, "kube.py")
            
            
if __name__ == "__main__":
    main()
