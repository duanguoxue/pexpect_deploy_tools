pexpect_deploy_tools
====================

批量远程操作脚本-- scp 和 ssh 


使用方法：
---------
当前目录创建 ip list：
192.168.0.100
192.168.0.101

pscp.py copy 本地文件到远程机器列表
-----------------------------------
pscp.py iplist.txt sourcefile destpath

rshell.py 远程机器上执行，本地脚本内容
--------------------------------------
rshell.py iplist.txt < test.sh



