#!/usr/bin/python3 
# Find Admin_Panel Files (@hackerone4x)
#------------------------------------------
# Eng : Abdulrahman Ayman Elshwehy --------
#------------------------------------------


import sys,argparse
import os
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from tkinter import *
from tkinter import ttk
import webbrowser
import subprocess

#os.system("cd KOP")
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[0m"


def findAdmin(url,file,output):
	f = open(file,'r');
	print(y+"\n\nAvilable links : \n")
	while True:
		sub_link = f.readline();out = open(output,'a');
		if not sub_link:
			break
		req_link = "http://"+url+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as s:
			continue
		except URLError as s:
			continue
		else:
			o = ("[@ "+r+"SUCSCESSFULL"+y+" @] >> "+g+req_link+y);outs = out.writelines(o);out.close();print(o)
def findAdmins(url,file,output):
	f = open(file,'r');
	print(y+"\n\nAvilable links : \n")
	while True:
		sub_link = f.readline();out = open(output,'a');
		if not sub_link:
			break
		req_link = "https://"+url+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as s:
			continue
		except URLError as s:
			continue
		else:
			o = ("[@ "+r+"SUCSCESSFULL"+y+" @] >> "+g+req_link+y);outs = out.writelines(o);out.close();print(o)
def GUI():
    win = Tk()

#Set the geometry
    win.geometry("700x250")

# Define a function to return the Input data
    def get_data():
        label.config(text= entry.get(), font= ('Helvetica 13'))
    
    def openwebpage():
        webbrowser.open(url=(entry.get()))
    defuiltOfile = "Data.txt"
    def Save():
        io = open(defuiltOfile,'a')
        io.writelines(entry.get())
        io.close()

    def Scan():
        returned_text = subprocess.check_output("nmap -Pn "+entry.get(), shell=True, universal_newlines=True)
        label.config(text=returned_text ,bg="yellow",fg="green")



    entry = Entry(win, width= 42)
    entry.place(relx= .5, rely= .5, anchor= CENTER)
    label= Label(win, text="", font=('Helvetica 13'))
    label.pack()
    url = entry.get()
    
    
    entry1 = Entry(win, width= 42)
    entry1.place(relx= .5, rely= .6, anchor= CENTER)
    dt = entry1.get()
    def admin():
        findAdmin(entry.get(),'Data.txt',entry1.get())
        returned_text1 = subprocess.check_output("python3 main.py -u "+entry.get()+" -f "+'Data.txt'+" -o "+entry1.get(), shell=True, universal_newlines=True)
    ttk.Button(win, text= "Run", command= admin).place(relx= .7, rely= .5, anchor= CENTER)
    bt1 = ttk.Button(text= "Save", command= Save).place(relx= .7, rely= .6, anchor= CENTER)
    bt2 = ttk.Button(text= "Open", command= openwebpage).place(relx= .7, rely= .7, anchor= CENTER)
    bt3 = ttk.Button(text= "Scan", command= Scan).place(relx= .7, rely= .8, anchor= CENTER)

    
    win.mainloop()

def banner():

    print(g+
    "###############################################################################\n"+
    "# "+b+"#### #### #### ####"+g+" #"+r+"         A"+b+"      PPPPPP"+w+"       WWW$"+b+"__HackerOne4x__$"+g+"      #\n"+
    "# "+b+"0000 0000 0000 0000"+g+" #"+r+"        AAA"+b+"     PP  PP"+w+"       #$%$%$ ANONYMOUS @#$"+g+"      #\n"+
    "# "+b+"@0@0 @0@0 @0@0 @0@0"+g+" #"+r+"       AAAAA"+b+"    PPPPPP"+w+"                                 "+g+"#\n"+
    "# "+b+"#### #### #### ####"+g+" #"+r+"      AAAAAAA"+b+"   PP    "+w+"   -- Find Admin Panel Files"+g+"     #\n"+
    "# "+b+"$$$$$$$$$$$$$$$$$$$"+g+" #"+r+"     AAAAAAAAA"+b+"  PP    "+w+"                                 "+g+"#\n"+
    "###############################################################################\n")
def help():
    print(b+"""
    +----------------------------------------------------------+
    | -h , --help      Display Help                            |
    | -f , --file      To Add Wordlist File                    |
    | -b , --banner    To Dispaly Banner                       |
    | -u , --url       To Request To Url              [ NEED ] |
    | -o , --output    To Write Output On File                 |
    | -g , --gui       To display App GUI                      |
    | -s , --scan      To Scan A URL                           |
    +----------------------------------------------------------+
    """)

parser = argparse.ArgumentParser()
parser.add_argument("-u","--url",help="To add page Url ")
parser.add_argument("-f","--file",help="Add File Or Wordlist To Write From")
parser.add_argument("-b","--banner",help="To Display The App Banner")
parser.add_argument("-o","--output",help="Add Output File To Save In")
parser.add_argument("-g","--gui",help="To Display The App GUI")
parser.add_argument("-m","--man",help="To Show The Maniual")
parser.add_argument("-s","--scan",help="Scannig The URL")

args = parser.parse_args()
try:
    if (args.url and args.file and args.output):
            findAdmin(args.url,args.file,args.output)
            findAdmins(args.url,args.file,args.output)
    elif args.banner == "show":
        banner()
    elif args.man == "help":
        help()
    elif args.gui == "start":
        GUI()
    elif (args.url and args.file):
        findAdmin(args.url,args.file,"Out.txt")
    elif (args.url and args.file and args.output):
        findAdmin(args.url,args.file,args.output)
        findAdmins(args.url,args.file,args.output)
    elif (args.url or args.man or args.banner or args.file or args.output or args.gui) == False:
        print("\n")
    elif args.scan:
        os.system("nmap -Pn "+args.scan)
    elif (sys.argv[0] == True) and (sys.argv[1] == False):
        print("\n")
    else:
        print(r+"$$ Error No Arguments !!")
except KeyboardInterrupt:
    os.system("clear")
    print(b+"Keyboard Interrupts")
    time.sleep(0.5)
    os.system("clear")
