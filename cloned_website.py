import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from tokenfinder import Tokenfinder

# URL of the web page you want to extract
url = "http://localhost:8000"
#url = "https://docs.microsoft.com/en-us/learn/modules/build-simple-website/"

# initialize a session
session = requests.Session()
# set the User-agent as a regular browser
session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

# get the HTML content
html = session.get(url).content

list_url = []

token = Tokenfinder.find_tokens_in_string(str(html))
if token:
    list_url.append(token)

# parse HTML using beautiful soup
soup = bs(html, "html.parser")

# get the JavaScript files
script_files = []

for script in soup.find_all("script"):
    if script.attrs.get("src"):
        # if the tag has the attribute 'src'
        script_url = urljoin(url, script.attrs.get("src"))
        script_files.append(script_url)

print("Total script files in the page:", len(script_files))

# write file links into files
#if len(script_files) > 0:
#    with open("javascript_files.txt", "w") as f:
i = 1
if len(script_files) > 0:
    for js_file in script_files:
        print("Going through file " + str(i))
        js_content = session.get(js_file).content
        for line in js_content:
            token = Tokenfinder.find_tokens_in_string(str(line))
            if token:
                list_url.append(token)
        i = i + 1

if len(list_url) > 0:
    for entry in list_url:
        print(entry)
else:
    print("No honeytoken found on this website")
