from wifi import Cell
import sys

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
    while True:
        # interface = input(r+"[ INTERFACE ]# " +b)
        interface = sys.argv[1]
        Lan = Cell.all(interface)
        if interface is None:
            continue
        elif interface == "":
            pass
        elif interface == " ":
            pass
        else:
            for i in Lan:
                print(y+"+-----------------------------------+")
                print(("| SSID         : {} ").format(i.ssid))
                print(("| SIGNAL       : {} ").format(i.signal))
                print(("| QUALITY      : {} ").format(i.quality))
                print(("| ENCRYPTED    : {} ").format(i.encrypted))
                print(("| ENCRYPT TYPE : {} ").format(i.encryption_type))
                print(("| MAC ADDRESS  : {} ").format(i.address))
                print(("| BIT RATES    : {} ").format(i.bitrates))
                print(("| MODE         : {} ").format(i.mode))
                print(("| NOISE        : {} ").format(i.noise))
                print(("| MODE         : {} ").format(i.mode))  
        print(y+"+-----------------------------------+")
except:
    print((r+" [x] Error "+y+"'{}'"+r+" Not Found !").format(interface))
    
