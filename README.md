pexpect_deploy_tools
====================

批量远程操作脚本-- scp 和 ssh 
无环境依赖，解压压缩包即可使用，较原生 expect 慢，可定制性高。

使用方法：
---------
当前目录创建 ip list：  
192.168.0.100  
192.168.0.101  

pscp.py 拷贝本地文件到远程机器(iplist.txt)列表的制定目录
-------------------------------------------------------
pscp.py iplist.txt source_localfile destpath  
说明：  
iplist.txt: 远程机器列表  
source_localfile: 需要拷贝的文件  
destpath: 远程目的路径  

rshell.py 远程机器上执行 test.sh
--------------------------------------
rshell.py iplist.txt < test.sh


