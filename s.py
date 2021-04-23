import socket
import sys
import time
import os
from threading import *
import pyfiglet
os.system('clear')
os.system('tput setaf 4')
title = pyfiglet.figlet_format("\t\t\t\t! UDP CHAT APP !", font= "bulbhead")
print(title)
print("************************************************************************")
print("************************************************************************")

def receiver(ip, port):
    myp = socket.SOCK_DGRAM
    afn = socket.AF_INET
    s = socket.socket(afn, myp)
    s.bind((ip, port))
    while True:
        x = s.recvfrom(1024)
        os.system("tput setaf 6")
        print('\t\t\t\t\t\t\tReceived Message : ',x[0].decode())
        os.system("tput setaf 6")
        time.sleep(2 / 10)

def sender(ip2, port2):
    myp = socket.SOCK_DGRAM
    afn = socket.AF_INET
    s = socket.socket(afn, myp)
    while True:
        os.system("tput setaf 5")
        msg = input()
        s.sendto(msg.encode(), (ip2, port2))
        os.system("tput setaf 5")
        print('Your Message : ', msg)
        os.system("tput setaf 5")
        time.sleep(0.2)

os.system("tput setaf 7")
sys.stdout.write("Enter your IP address: ")
sys.stdout.flush()
ip = sys.stdin.readline()
port = int(input('Enter your port number : '))
os.system("tput setaf 2")
sys.stdout.write("Enter your Friend's IP address : ")
sys.stdout.flush()
ip2 = sys.stdin.readline()
port2 = int(input("Enter your Friend's port number : "))
os.system("tput setaf 3")
print("----------------------------------------------------------------------")
print("\t\t\t\tSTART CHATTING")
print("\n----------------------------------------------------------------------")
os.system('tput setaf 4')
t1 = Thread(target=sender, args=(ip2, port2))
t2 = Thread(target=receiver, args=(ip, port))

t1.start()
t2.start()
