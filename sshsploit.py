#!/usr/bin/env python3

#            ---------------------------------------------------
#                            SSHSploit Framework                                                                  
#            ---------------------------------------------------
#                Copyright (C) <2019-2020>  <Entynetproject>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

os.system("printf '\033]2;Ghost Framework\a'")

import sys
import subprocess
import readline
import time

Q = '\033[1;77m[?] \033[0m'
G = '\033[1;34m[*] \033[0m'
S = '\033[1;32m[+] \033[0m'
W = '\033[1;33m[!] \033[0m'
E = '\033[1;31m[-] \033[0m'

readline.parse_and_bind("tab: complete")

def banner():
    os.system("clear")
    os.system("cat banner/banner.txt")
    print("")
    print("SSHSploit Framework v1.0")
    print("------------------------")
    print("")

def main():
    ui = input('\033[4msshsploit\033[0m> ').strip(" ")
    ui = ui.split()
    while True:
        if ui == []:
            pass
        elif ui[0] == "exit":
            os.system("chmod +x core/server.sh && core/server.sh stop")
            sys.exit()
        elif ui[0] == "clear":
            os.system("clear")
        elif ui[0] == "update":
            os.system("chmod +x etc/update.sh && etc/update.sh")
        elif ui[0] == "help":
            print("")
            print("Core Commands")
            print("=============")
            os.system("cat data/cmds/core_cmds.txt")
            print("")
        else:
            print(E+"Unrecognized command!")
        ui = input('\033[4msshsploit\033[0m> ').strip(" ")
        ui = ui.split()
