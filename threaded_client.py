import socket
import threading
import time
import sys

from _thread import *

# thread fuction 
def threaded(c): 
    while (c): 
        try:
	    # Data received from server. 
            msg = c.recv(1024).decode() + "\n> "
            sys.stdout.write(msg)
        except:
            break 
        


def Main():

    # Connection setup.
    s = socket.socket()
    port = 1200                
    s.connect('73.165.28.234', port)  

    # Enter the room.
    name = input("Connected, please input a screen-name: ")
    print("Hello, " + name + ". Try sending a message! Type 'quit' to exit.")
    s.send(("> " + name + " has joined.").encode())

    # Start a new thread and return its identifier 
    start_new_thread(threaded, (s,)) 

    # a forever loop until client wants to exit 
    while True:  
        mes = input("> ")
        if mes == "quit":
            break
        s.send((name + ": " + mes).encode())

    s.send("quit".encode())
    s.close() 
    print("Exiting...")


if __name__ == '__main__': 
	Main() 
