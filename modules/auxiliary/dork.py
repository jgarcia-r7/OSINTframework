#!/usr/bin/env python3
# Module: Google Dorking Module
# Author: Jessi
from colorama import Fore, Style
from googlesearch import search
from time import sleep

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

# Dork class.
class pyDork:

    # Module specific settings.
    query = ''
    limit = 10
    outfile = 'google_dork.txt'

    @classmethod
    def print_help(cls):
        module_help = f"""

Module Options (auxiliary/google_dork):
                
    Name                  Description                 Current Setting
    ----                  -----------                 ---------------
    QUERY                 Desired query               {cls.query}
    LIMIT                 Results limit               {cls.limit}
    OUTFILE               Output file                 {cls.outfile}

                """
        print(module_help)

    @classmethod
    def init_query(cls):
        f = open(cls.outfile, "wt")
        for result in search(cls.query, num_results=cls.limit):
            print(GREEN + "[+]" + RST + " {}".format(result))
            f.write(result + "\n")
            sleep(.30)
        print(GREEN + "[+]" + RST + " Results written to {}\n".format(cls.outfile))


def main():
    print(BLUE + "\n[*]" + RST + " Running query: " + pyDork.query + " with limit " + str(pyDork.limit) + "...")
    pyDork.init_query()
