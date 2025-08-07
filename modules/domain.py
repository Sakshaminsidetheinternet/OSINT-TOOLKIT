# modules/domain_enum.py
import whois
import requests

def enumerate_domain(domain):
    print(f"Looking up WHOIS info for: {domain}")
    try:
        w = whois.whois(domain)
        print(f"Registrar: {w.registrar}")
        print(f"Created: {w.creation_date}")
        print(f"Updated: {w.updated_date}")
    except Exception as e:
        print(f"[!] WHOIS failed: {e}")

    print("Checking subdomains via crt.sh")
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url, timeout=10)
        data = response.json()
        found = set(entry['name_value'] for entry in data)
        for sub in found:
            print(f"[+] {sub}")
    except Exception as e:
        print(f"[!] Subdomain enum failed: {e}")
