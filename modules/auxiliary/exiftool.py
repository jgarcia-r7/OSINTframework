#!/usr/bin/env python3
# Module: ExifTool
# Author: Jessi
# REQUIRES EXIFTOOL INSTALLED (apt install libimage-exiftool-perl)

import os
from time import sleep
import subprocess
import simplejson
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

# Exiftool class
class ExifTool(object): # Define ExifTool class.

    exiftool_bin = os.popen('which exiftool').read().strip()

    sentinel = "{ready}\n"

    def __init__(self, executable=exiftool_bin):
        self.executable = executable

    def __enter__(self):
        self.process = subprocess.Popen(
            [self.executable, "-stay_open", "True",  "-@", "-"],
            universal_newlines=True,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        return self

    def  __exit__(self, exc_type, exc_value, traceback):
        self.process.stdin.write("-stay_open\nFalse\n")
        self.process.stdin.flush()

    def execute(self, *args):
        args = args + ("-execute\n",)
        self.process.stdin.write(str.join("\n", args))
        self.process.stdin.flush()
        output = ""
        fd = self.process.stdout.fileno()
        while not output.endswith(self.sentinel):
            output += os.read(fd, 4096).decode('utf-8')
        return output[:-len(self.sentinel)]

    def get_metadata(self, outdir, o):
        o.write(simplejson.dumps(simplejson.loads(self.execute("-Author", "-Creator", "-LastModifiedBy", "-J", outdir)), indent=4, sort_keys=True))

    
    
def main(outfile, outdir):
    print(BLUE + "[*]" + RST + " Extracting metadata...")
    sleep(2)
    o = open(outfile, 'w+')
    with ExifTool() as e:
        e.get_metadata(outdir, o)
    print(GREEN + "[+]" + RST + " Extracted metadata written to {}!\n".format(outfile))
