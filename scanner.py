

import sys
import socket
from datetime import datetime


#Defining target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
        print('\033[31m' + "Invalid amount arguments (?︵?)")
        print("Syntax: Python3 scanner.py <ip> ヽ(*｀ﾟД´)ﾉ" + '\033[0m')

#pwetty banner :3
print("\033[93m･:*:･ﾟ★,｡･:*:･ﾟ☆\033[0m" * 5)
print("\033[1m\033[95mScanning target: \033[0m"+target)
print("\033[3mTime started: "+str(datetime.now()))
print("\033[93m･:*:･ﾟ★,｡･:*:･ﾟ☆\033[0m" * 5)

#searching @.@
try:
        for port in range(50,85):
               s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               socket.setdefaulttimeout(1)
               result = s.connect_ex((target,port))
               if result ==0:
                      print('\033[1m\033[32m' + f"Port {port} is open" + '\033[0m')
        s.close()

#control c typpa thangs               
except KeyboardInterrupt:
       print('\033[1m\033[34m' + "\nExiting program ..・ヾ(。＞＜)シ")
       sys.exit()

except socket.gaierror:
       print('\033[31m' + "Hostname could NOT be resolved (x_x)")
       sys.exit()

except socket.error:
   print('\033[31m' + "Could NOT connect to server (x_x)")
   sys.exit()
