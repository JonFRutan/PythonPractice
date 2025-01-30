# Grabs raw html from a given link.
# Link must adhere to regex below.
import requests, sys, re

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = input("Paste a Url: ")
    
url_pattern = r"https?:\/\/[a-zA-Z0-9]+\.[a-zA-Z]+"
url_check = True

while url_check:
    if re.search(url_pattern, url):
        url_check = False
        pass
    else:
        print("Your URL format is incorrect, make sure to include https or http, and a domain.\n")
        url = input("Paste a Url: ")
    
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    print(html_content)
    print()
    save = input("Save to file? (y/n)")
    if save == 'y':
        with open("output.html", "w") as file:
            file.write(html_content)
            exit()
    else:
        exit()
else:
    print(f"Error: {response.status_code}")
