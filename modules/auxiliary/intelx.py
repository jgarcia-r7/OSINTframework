#!/usr/bin/env python3
# Module: Intelx
from ast import In
import requests
from colorama import Fore, Style


# Define colorama colors.
GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE
WHITE = Fore.WHITE
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
PINK = Fore.MAGENTA
BRIGHT = Style.BRIGHT
DIM = Style.DIM
NORM = Style.NORMAL
RST = Style.RESET_ALL

# intelx class
class IntelX:

    api_key = ''
    api_url = '2.intelx.io'
    headers = {"User-Agent": "Mozilla/5.0", "Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Origin": "https://phonebook.cz", "Referer": "https://phonebook.cz/", "Content-Type": "application/x-www-form-urlencoded"}

    domain = ''
    limit = 10
    outfile = '_emails.txt'

    @classmethod
    def print_help(cls):
       module_help =f"""

Module Options (auxiliary/intelx_search):
                
    Name                  Description                 Current Setting
    ----                  -----------                 ---------------
    API_KEY               IntelX API Key              {cls.api_key}
    DOMAIN                Target domain               {cls.domain}
    LIMIT                 Results limit               {cls.limit}
    OUTFILE               Output file                 {cls.outfile}

       """
       print(module_help)
   
    @classmethod
    def search(cls):

        key_payload = {"k":cls.api_key}
        data_payload = {"maxresults": cls.limit, "media": 0, "target": 2, "term": cls.domain, "terminate": [None], "timeout": 20}
        r_id = requests.post(f'https://{cls.api_url}/phonebook/search', headers=cls.headers, params=key_payload, json=data_payload)
        id = r_id.json()["id"]
        print(GREEN + "[+]" + RST + " Search ID Retrieved: {}".format(id))

        results_payload = {"k":cls.api_key, "id":id, "limit": cls.limit}
        r_results = requests.get(f'https://{cls.api_url}/phonebook/search/result', headers=cls.headers, params=results_payload)
        storage = r_results.json()

        w = open(cls.outfile, 'w+')
        for each in storage["selectors"]:
            w.write(each["selectorvalue"])
            w.write("\n")
        w.close()

        emailSum = 0
        with open(cls.outfile) as emails:
            for email in emails:
                if email.strip():
                    emailSum += 1
        print(GREEN + "[+]" + RST + " Found {} email addresses!".format(emailSum))
        print(GREEN + "[+]" + RST + " Results written to {}\n".format(cls.outfile))


def main():
    print(BLUE + "\n[*]" + RST + " Searching for email addressess for domain: " + IntelX.domain + " with limit " + str(IntelX.limit) + "...")
    IntelX.search()
