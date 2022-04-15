#!/usr/bin/env python3
# Module: extraMetaPy: Module of extraMetaPy
# Author: Jessi
# REQUIRES EXIFTOOL INSTALLED (apt install libimage-exiftool-perl)

import sys
import os
import argparse
from time import sleep
import subprocess
import simplejson
import urllib.request
from googlesearch import search
from colorama import Fore, Style
from urllib.parse import urlparse
from datetime import datetime


# Define colorama colors.
GREEN = Fore.GREEN
RED = Fore.RED
WHITE = Fore.WHITE
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
PINK = Fore.MAGENTA
BRIGHT = Style.BRIGHT
DIM = Style.DIM
NORM = Style.NORMAL
RST = Style.RESET_ALL

# extrametapy module class
class extraMetaPy:

    # Module specific settings.
    domain = ''
    filetypes = list(('pdf, doc, docx, xls, xlsx, ppt, pptx, pub, csv').split(', '))
    limit = 10
    outfile = '{}_meta.json'.format(domain)
    outdir = '{}_files/'.format(domain)
    urllist = '{}_urls.txt'.format(domain)

    @classmethod
    def print_help(cls):
        help_screen = f"""

Module Options (auxiliary/extrametapy):

    Name                  Description                 Current Setting
    ----                  -----------                 ---------------
    DOMAIN                Target domain               {cls.domain}
    FILETYPES             Filetypes to dork           {cls.filetypes}
    LIMIT                 Results limit               {cls.limit}  
    OUTFILE               Output file                 {cls.outfile}
    OUTDIR                Directory for files         {cls.outdir}
    URLLIST               File to store URLs          {cls.urllist}

        """
        print(help_screen)

    @classmethod
    def create_dir(cls):
        if not os.path.exists(cls.outdir):
            os.makedirs(cls.outdir)

    @classmethod
    def dork(cls): # Google Dork function.
        with open(cls.urllist, 'a+') as url_store:
            for ft in cls.filetypes:
                query = 'site:' + cls.domain + ' filetype:' + ft
                print(GREEN + "[+]" + RST + " Dorking domain: " + cls.domain + " for " + ft + " files")
                try:
                    for result in search(query, num_results=cls.limit):
                            url_store.write(result + "\n")
                except:
                    print(f'{RED}{BRIGHT}[X]{RST} {WHITE}Dork failed for: {BRIGHT}{ft}{RST}')
                    print(f'{DIM}Failure is likely due to too many requests...')
                    print(f'Try again later\n{RST}')

    @classmethod
    def count_urls(cls):
        url_sum = 0
        with open(cls.urllist, "r") as url_list:
            for url in url_list:
                if url.strip():
                    url_sum += 1

        print(GREEN + "[+]" + RST + " Scraped {} URLs!".format(url_sum))

    @classmethod
    def download_url(cls): # Download files function.
        with open(cls.urllist) as urls:
            for i in urls:
                url = i.strip()
                name = url.rsplit('/', 1)[1]
                filename = cls.outdir + name
                opener = urllib.request.build_opener()
                opener.addheaders = [('User-agent', 'Mozilla/5.0')] # Set our download function to use Mozilla user-agent to avoid being blocked.
                urllib.request.install_opener(opener)
                for i in range(0,3): # Try to download the file 3 times.
                    try:
                        r = urllib.request.urlretrieve(url, filename)
                    except urllib.error.HTTPError as exception:
                        if i == 2:
                            print(RED + "[-]" + RST + " Download failed for "+ url + " (" + DIM + str(exception) + RST + ")")
                    except urllib.error.ContentTooShortError as exception:
                        if i == 2:
                            print(RED + "[-]" + RST + " Download failed for "+ url + " (" + DIM + str(exception) + RST + ")")
                    except:
                        if i == 2:
                            print(RED + "[-]" + RST + " Download failed for " + url + " (" + DIM + "Unknown error" + RST + ")")
                    else:
                        print(GREEN + "[+]" + RST + " Downloaded: {}".format(url))
                        break

    @classmethod
    def count_files(cls):
        dir_count = 0
        dir_listing = os.listdir(cls.outdir)
        for num in dir_listing:
            if num:
                dir_count += 1
        print(GREEN + "[+]" + RST + " Downloaded {} files to {}".format(dir_count,cls.outdir))


def main():
    extraMetaPy.create_dir()
    print(CYAN + "\n[*]" + RST + " Google Dorking for specified filetype(s) on domain: " + extraMetaPy.domain + " with limit " + str(extraMetaPy.limit) + "...")
    extraMetaPy.dork()
    extraMetaPy.count_urls()
    print(GREEN + "[+]" + RST + " URLs written to {}".format(extraMetaPy.urllist))
    print(CYAN + "[*]" + RST + " Downloading files...")
    extraMetaPy.download_url()
    extraMetaPy.count_files()
