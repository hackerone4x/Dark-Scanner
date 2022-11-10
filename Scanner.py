import socket
from geoip import geolite2
import sys,os,subprocess,time
#############################


# Colors :
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[0m"
try:
    # targetn = input(r+"[ TARGET ]# "+y)
    targetn = sys.argv[1]
    target = socket.gethostbyname(targetn)
    p = 80
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    r = s.connect_ex((target,p))
    ports = [80,443,23,14,2,500,22,1,3,3333,4444,550]
    print(b+"+---------- STARTED -----------+")
    for i in ports:
        if r  == 0:
            service = socket.getservbyport(i)
            print((" {} --------> {} ").format(i,service))
        s.close
        print("--------------------------------")
    i = input(">")
    if i == "q":
        exit()
    # os.system('read -p "Press [Enter] key to start backup..."')
except:
    pass
