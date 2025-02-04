# Grabs raw html from a given link.
# Link must adhere to regex below.
import requests, sys, re

def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Paste a Url: ")
    grabber(url)

def grab_from_id(app_id):
    url = f"https://store.steampowered.com/app/{app_id}/"
    grabber(url)
    
def grabber(url):
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
#    print(html_content)
#    print()
        save = input("Save to file? (y) ")
        if save == 'y':
            with open("outputs/output.html", "w") as file:
                print("Created output.html")
                file.write(html_content)
                exit()
        else:
            exit()
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    main()
