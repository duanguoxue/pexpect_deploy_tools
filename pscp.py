#!/usr/bin/env python
# -*- coding: utf8 -*-
# author : duanguoxue
# date : 2014-06-22

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import sys
import os
import getpass
import signal
sys.path.append(os.getcwd() + '/pexpect-3.3')
import pexpect
import traceback
# Note that, for Python 3 compatibility reasons, we are using spawnu and
# importing unicode_literals (above). spawnu accepts Unicode input and
# unicode_literals makes all string literals in this script Unicode by default.

def ScpCmdParam(username, passwd, iphost, filename, destpath):
    '''username 目的用户名
       passwd 目的用户密码
       iphost 目的主机地址
       filename 源文件名称
       destpath 目的文件路径
    '''
    scpcmd="scp %s %s@%s:%s"%(filename,username,iphost,destpath)
    ScpCmd(passwd, scpcmd)


def ScpCmd(passwd, scpcmd):
    print (scpcmd)
    child = pexpect.spawnu(scpcmd)
    while 1:
        scp_savekey="Are you sure you want to continue connecting (yes/no)?"
        index=child.expect([scp_savekey, "password:", pexpect.TIMEOUT,pexpect.EOF])
        #print ("index:%s"%index)
        if index == 0:
            print ("pexpect send yes")
            child.sendline('yes')
        if index == 1:
            print ("pexpect send passwd")
            child.sendline(passwd)
        if index == 2:
            print ("pexpect timeout")
            break
        if index == 3:
            #print ("pexpect eof")
            break
    child.close()
    print ("scp ok.")


def read_ip_list(filename, srcfilename, destpath):
    passwd = getpass.getpass('password: ')
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            ip = line.replace("\r\n","")
            ip = ip.replace("\n","")
            if len(ip)==0 or (len(ip)!=0 and ip[0]=='#'):
                continue
            try:
                if len(ip.split('.')) != 4:
                    print("error ip:".join(ip))
                    break
                ScpCmdParam("admin", passwd, ip, srcfilename, destpath)
                count += 1
            except:
                print (ip,"timeout")
                print (traceback.print_exc())
    print("total ipcount:%d" % count)

def handler(signum, frame):
    print ('\nctrl C exit(%d)'%signum)
    sys.exit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler)
    if len(sys.argv) != 4:
        print("%s iplist.txt source_file dest_path "%sys.argv[0])
        sys.exit()
    read_ip_list(sys.argv[1], sys.argv[2], sys.argv[3])

