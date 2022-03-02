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


def run_process(file, string_to_search, script):
    p = subprocess.run([f"python3 {script} -f {file} -s {string_to_search}"],
                       shell=True, capture_output=True, text=True)
    print(f"Return code: {p.returncode}")
    print(f"Stdout:\n{p.stdout}")
    if p.returncode == 0 and "detected" in p.stdout:
        print(f"{os.path.join(os.getcwd(), file)} is a honeytoken.")


def main():
    print("-------- START SCRIPT  --------")
    file = input("Enter filename or full path: ")
    if os.path.exists(file):
        string_to_search = input("Enter domain or string you want to look for in the file: ")
    else:
        print("File not found. Check the path.")
        exit(1)

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
        run_process(file, string_to_search, "docx.py")

    elif ".sql" in type:
        print("SQL file found.")
    #     ask the administration to keep the windows open ( or at least make a button to control each window)

    elif ".conf" in type:
        print("Configuration file found.")

    elif "_" in type or "" in type:
        print("No file extension.")
        if is_wireguard_file(file):
            run_process(file, string_to_search, "wg.py")
        if is_kubeconfig_file(file):
            print("Kubernetes config file detected")
            run_process(file, string_to_search, "kube.py")


if __name__ == "__main__":
    main()
