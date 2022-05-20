# -*- encoding: utf-8 -*-
import os
import subprocess
import validators


def get_type(file):
    print("-------- GET FILE EXTENSION  --------")
    file_name, file_extension = os.path.splitext(file)
    print("Filename: ", file_name)
    print("File extension: ", file_extension)
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
    # Windows - does not support calling executables directly
    print("-------- LAUNCHING CHILD SCRIPT --------")
    if os.sys.platform == "win32":
        subprocess.run(['cmd', '/c', ["python3 %s -f %s" % (script, file)]])
    else:
        subprocess.run(["python3 %s -f %s" % (script, file)], stdout=True, shell=True)


def main():
    print("-------- START MASTER SCRIPT  --------")
    file = input("Enter filename or full path: ")
    # if the input is an url, launch cloned website
    if validators.url(file):
        run_process(file, "cloned_website.py")
        return (0)
    else:
        if not os.path.exists(file):
            print("File not found. Check the path.")
            return (1)

    type = get_type(file)
    # print("-------- GET FILE EXTENSION  --------")

    if ".txt" in type:
        print("Text file found.")
        run_process(file, "textfinder.py")

    elif ".pdf" in type:
        print("Pdf file found.")
        run_process(file, "pdf.py")

    elif ".xlsx" in type:
        print("Excel file found.")
        run_process(file, "office_docx.py")
    elif ".docx" in type:
        print("Word document found.")
        run_process(file, "office_docx.py")

    elif ".exe" in type:
        print("Executable file found.")
        run_process(file, "exe.py")

    elif ".sql" in type:
        print("SQL file found.")
        run_process(file, "sql_dump_checker.py")

    elif ".ini" in type:
        print("Ini file found")
        run_process(file, "windows_folder.py")

    elif ".conf" in type:
        print("Configuration file found.")

    elif ".png" in type:
        print("Png file found")
        run_process(file, "qrcode.py")

    elif "_" in type or "" in type:
        print("No file extension.")
        if is_wireguard_file(file) or is_kubeconfig_file(file):
            run_process(file, "conf_files.py")


if __name__ == "__main__":
    main()
