# Importing Required Modules
import socket as s
import threading as thd
import os
import pyfiglet
os.system("cls")
os.system("color 2")
title = pyfiglet.figlet_format("\t\t\t\t! UDP CHAT APP !", font= "bulbhead")
os.system("color 2")
print( title)
print("***********************************************************************************************")
print("***********************************************************************************************")
os.system("color 8")
print("\n\t\t\t\t\tSTART CHATTING")
os.system("color 8")
print("------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------")


# Create a Socket and Bind IP and PORT to It
skt = s.socket(s.AF_INET, s.SOCK_DGRAM)
localIP = "192.168.1.5"
skt.bind((localIP, 2222))

# Get Partner's IP to chat with
usrIP = "192.168.1.6"
print()

# Function to Recieve and Print the Message
def recv_msg():
    while True:
        os.system("color 5")
        msgRcv = skt.recvfrom(1024)
        if msgRcv[0].decode() == "quit" or msgRcv[0].decode() == "bye":
            print("Now your friend is Offline!")
            os._exit(1)
        print("\n\t\t\t\t\t\t\t\t\t" + msgRcv[1][0] + ": " + msgRcv[0].decode())


# Function to Send the Message
def send_msg():
    while True:
        data = input().encode()
        msgSent = skt.sendto(data, (usrIP, 2222))
        if data.decode() == "quit":
            os._exit(1)

# Thread for Send Message Function
send_thd = thd.Thread(target=send_msg)

# Threads for Recieve Message Function
rcv_thd = thd.Thread(target=recv_msg)

# Starting Threads
send_thd.start()
rcv_thd.start()