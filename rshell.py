#!/usr/bin/env python
# author : duanguoxue
# date : 2014-06-10
# remote  execute shell
from __future__ import print_function
from __future__ import absolute_import

import os, sys, getpass, signal
sys.path.append(os.getcwd() + '/pexpect-3.3')
import pexpect, pxssh
import traceback

def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line

def execute_cmd(hostname, username, password, cmdlist):
    # Login via SSH
    print("hostname:", hostname)
    p = pxssh.pxssh()
    p.login(hostname, username, password)

    for line in cmdlist:
        if len(line)==0 or line=='\n':
            continue
        p.sendline(line.replace('\n',''))
        p.prompt()
        result = p.before
        print ( result.split('\r\n') )
    p.logout()

def read_ip_list(filename, cmdlist):
    password = getpass.getpass('password: ')
    for line in read_file(filename):
        ip = line.replace("\r\n","")
        ip = ip.replace("\n","")
        if len(ip)==0 or (len(ip)!=0 and ip[0]=='#') :
            continue
        try:
            if len(ip.split('.')) != 4:
                print("error ip:".join(ip))
                break
            execute_cmd(ip, "admin", password, cmdlist)
        except:
            print (ip,"timeout")
            traceback.print_stack()

def handler(signum, frame):
    print ('\nctrl C exit(%d)'%signum)
    sys.exit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler)
    if len(sys.argv) < 2:
        print ("%s iplist.txt cmd | <rtest.sh"%sys.argv[0])
        sys.exit()
    # read cmd from stdin
    if len(sys.argv) == 2:
        cmdlist=[]
        for line in sys.stdin:
            cmdlist.append(line)
        read_ip_list(sys.argv[1], cmdlist)
    # read from cmd param
    if len(sys.argv) == 3:
        read_ip_list(sys.argv[1], [sys.argv[2]])

