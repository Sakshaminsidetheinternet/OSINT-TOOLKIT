# main.py

import argparse
from modules import username, email_lookup, domain

def main():
    parser = argparse.ArgumentParser(description="Simple OSINT Automation Toolkit")
    parser.add_argument('--username', help="Username to search for")
    parser.add_argument('--email', help="Email to check for leaks")
    parser.add_argument('--domain', help="Domain to enumerate")

    args = parser.parse_args()

    if args.username:
        username.search_username(args.username)

    if args.email:
        email_lookup.check_email(args.email)

    if args.domain:
        domain.enumerate_domain(args.domain)

if __name__ == "__main__":
    main()
