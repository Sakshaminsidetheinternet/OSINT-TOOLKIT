# modules/email_lookup.py

def check_email(email):
    print(f"Checking if {email} has been in a data breach...")
    # Simulation
    leaked_emails = ["admin@example.com", "user123@gmail.com"]
    if email in leaked_emails:
        print(f"[!] {email} FOUND in data breach (simulated)")
    else:
        print(f"[-] {email} not found in known breaches (simulated)")
