import sys,os,subprocess

PACKET_FILE = "Packets.Pack"

SysName = subprocess.getoutput("uname -n")

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


# Config :
defuilt_out = "Out.req"
defuilt_worlist = "Data.txt"
defuilt_port = 80
defuilt_name = 'Dark-Scanner'


# Help :
HELP = (b+'''
        +---------------------------+
        |Commands On Dark-Scanner : |
        |---------------------------+
        |help    | to Show Help     |
        |scan    | Do port Scan     |
        |sniff   | Monitor Pkts     |
        |shell   | Open Shell       |
        |show    | To Show Networks |
        |sco     | Out Scan         |
        |sno     | Out Sniff        |
        |hack    | Hacking #        |
        |req     | Show Panel       |
        |exit    | Exit Scanner     |
        ----------------------------
        '''+g)


    # Shell = input((r+" [ "+d+"Dark Scanner"+r+" ]"+b+"#"+y+"["+b+" {} "+y+"] "+g).format(r+SysName))
try:
    while True:
        Shell = input((r+" [ "+d+"Dark Scanner"+r+" ]"+b+"#"+y+"["+b+" {} "+y+"] ").format(r+SysName))
        if Shell == "scan":
            TargetH = input(r+" [+] [ TARGET ]# "+g)
            os.system(f"xterm -T 'Scanner' -hold -e python3 Scanner.py {TargetH}")
        elif Shell == "sniff":
            Sniffer_interface = input(r+"Enter Your Name OF Lan Card : "+y)
            os.system(("xterm -T 'Sniffer' -e python3 Sniffer.py {}".format(Sniffer_interface)))
        elif Shell == "shell":
            os.system("xterm -T 'Shell' -fg red -e python3 Info.py")
        elif Shell == "show":
            lan_network = input(r+" [+] [INTERFACE]# "+g)
            os.system(f"xterm -T 'Lan' -hold -g '38x52' -e python3 lan.py {lan_network} ")
        elif Shell == "help":
            print(HELP)
        elif Shell == "req":
            UrlInput = input(r+"[ URL ]# ")
            os.system("xterm -T 'Request Panel ' -e python3 Request.py -u {} -f {} -o Output.uls".format(UrlInput,defuilt_worlist))
        elif Shell == "hack":
            TargetH = input(r+" [+] [ TARGET ]# "+g)
            lan_network = input(r+" [+] [INTERFACE]# "+g)
            os.system(("xterm -T 'Scanner' -hold -e python3 Scanner.py {} & xterm -T 'Sniffer' -e python3 Sniffer.py {} & xterm -T 'Shell' -fg red -e python3 Info.py & xterm -T 'Lan' -hold -g '38x52' -e python3 lan.py {} & xterm -T 'Request Panel' -e python3 Request.py -u {} -f Filenames_Doted_Common.wordlist -o Output.uls").format(TargetH,lan_network,lan_network,TargetH))
        elif Shell == "sno":
            Sniffer_interface = input(r+"Enter Your Name OF Lan Card : "+y)
            os.system(f"python3 Sniffer.py {Sniffer_interface} > Packets.pkt")
        elif Shell == "sco":
            TargetH = input(r+" [+] [ TARGET ]# "+g)
            os.system(f"python3 Scanner.py {TargetH} > Scan.lc")
        elif Shell == "\n":
            pass
        elif Shell == "":
            pass
    # elif Shell not in ["help","\n","sno","sco","lan","show","sniff","shell","hack","scan"," ",""]:
    #     print((r+" ' "+y+"{} "+r+"' Is Not Defined ."+g).format(Shell))
    #     print(HELP)
    # elif Shell == " " or None or "":
    #     pass
        elif Shell == "exit":
            exit()
        else:
            print((r+" ' "+y+"{} "+r+"' Is Not Defined ."+g).format(Shell))
            print(HELP)
except KeyboardInterrupt:
    print("\n")
    print(r+"["+y+"!"+r+"] "+b+"Keyboard Interrupt !"+g)

# os.system("xterm python3 Info.py")
