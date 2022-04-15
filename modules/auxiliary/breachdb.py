#!/usr/bin/env python3
# Module: BreachDB
# Author: Jessi

import requests
from time import sleep
import json
from collections import Counter
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

# BreachDB Class
class BreachDB:

    apiurl = 'https://pwnd.tiden.io/search'
    domain = ''
    api_key = ''
    limit = 10
    outfile = '_breach.txt'

    @classmethod
    def print_help(cls):
        module_help = f"""

Module Options (auxiliary/breachdb):

    Name                  Description                 Current Setting
    ----                  -----------                 ---------------
    API_KEY               BreachDB API Key            {cls.api_key}
    DOMAIN                Target domain               {cls.domain}
    LIMIT                 Results limit               {cls.limit}
    OUTFILE               Output file                 {cls.outfile}

        """
        print(module_help)

    @classmethod
    def init_query(cls):
        headers = {"User-Agent": "Mozilla/5.0", "Authorization": "apikey {}".format(cls.api_key)}
        params = {"domain": cls.domain, "limit": cls.limit}
        sleep(2)

        r = requests.get(cls.apiurl, headers=headers, params=params)
        data = r.json()

        results = 0
        for d in data:
            results += 1
        print(GREEN + "[+]" + RST + " Found {} entries for {}!".format(results, cls.domain))
    
    # Data functions.
        results_table = []
        password_table = []

        for entry in data:
            username = []
            password = []
            username.append(entry["username"])
            password.append(entry["password"])
            results_table.append(f'{username}:{password}')
            password_table.append("".join(password))

    # Formatting
        common_passwords = Counter(password_table).most_common(3)
        commonpw_table = ["%i. %s" % (index + 1, value) for index, value in enumerate(common_passwords)]
        finalpw_table = "\n".join(commonpw_table)

        final_table = ",".join(results_table).replace("[","").replace("]","").replace(",","\n").replace("'","")

    # Write to outfile.
        with open(cls.outfile,"wt") as results_file:
            results_file.write(final_table)

        print(BLUE + "[*]" + RST + " Top 3 Passwords for {}".format(cls.domain))
        print(finalpw_table.replace("(","").replace(")","").replace(","," :").replace("'",""))
    
        print(GREEN + "[+]" + RST + " Results written to {}\n".format(cls.outfile))


def main():
    print(BLUE + "\n[*]" + RST + " Querying pwnd.tiden.io for domain: " + BreachDB.domain + " with limit " + str(BreachDB.limit) + "...")
    BreachDB.init_query()
