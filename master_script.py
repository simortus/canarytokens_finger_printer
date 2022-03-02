import os
import subprocess

def get_type(file):
    print("-------- GET TYPE  --------")
    file_name, file_extension = os.path.splitext(file)
    print(f"Filename: {file_name}")
    print(f"File extension: {file_extension}")
    return(file_extension)

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
    match type:
        case ".txt":
            print("Text file found.")
        case ".pdf":
            print("It's a damn pdf bro.")
        case ".xlsx":
            print("Excel document found.")
            p = subprocess.run([f"python3.10 office_docx.py -f {file} -s {string_to_search}"],
                               shell=True, capture_output=True, text=True)
        case ".docx":
            print("Word document found.")
            p = subprocess.run([f"python3.10 office_docx.py -f {file} -s {string_to_search}"],
                               shell=True, capture_output=True, text=True)
        case ".sql":
            print("SQL file found.")
            p = subprocess.run([f"python3.10 sql_dump_checker.py -f {file} -s {string_to_search}"],
                               shell=True, capture_output=True, text=True)
        case ".conf":
            print("Configuration file found.")
        case _:
            print("No file extension.")

    print(f"Return code: {p.returncode}")
    print(f"Stdout:\n{p.stdout}")
    if p.returncode == 0 and "detected" in p.stdout:
        print(f"{os.path.join(os.getcwd(), file)} is a honeytoken.")

if __name__ == "__main__":
    main()
