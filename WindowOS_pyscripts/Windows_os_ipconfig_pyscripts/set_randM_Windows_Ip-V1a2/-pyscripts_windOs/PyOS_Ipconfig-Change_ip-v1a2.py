'''
File Name: PyOS_Ipconfig-Change_ip

Name: Python OS Ipconfig command: change ip addres

Desc: Change ip address for Windows OS

'''
import os

wnds_change_ips_cmds = ['ipconfig /releae','ipconfig /renew']

for cmd in wnds_change_ips_cmds:

    os.system(cmd)
    
print('\n- IP RENEWED!!!')

#input("\n_> press 'Enter' to close.. ")


