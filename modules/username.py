# modules/username_scan.py
import requests

def search_username(username):
    print(f"Searching for username: {username}")
    platforms = {
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Instagram": f"https://www.instagram.com/{username}"
    }

    for site, url in platforms.items():
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"[+] Found on {site}: {url}")
            else:
                print(f"[-] Not found on {site}")
        except Exception as e:
            print(f"[!] Error checking {site}: {e}")
