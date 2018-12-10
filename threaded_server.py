# import socket programming library 
import socket
import threading

from _thread import *

clients = []

# thread fuction 
def threaded(c): 
    while True: 

		# data received from client 
        try:
            data = c.recv(1024)
        except:
            break

        if data == "quit":
            c.close()
            break

        if not data: 
            print('Bye') 
            break

        for client in clients:
        #    if c != client:
            try:
                client.send(data)
            except:
                clients.remove(client)


def Main(): 
    host = "" 

	# reverse a port on your computer 
	# in our case it is 12345 but it 
	# can be anything 
    port = 25565
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to post", port) 

	# put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 

	# a forever loop until client wants to exit 
    while True: 

		# establish connection with client 
        c, addr = s.accept() 

		# lock acquired by client 
        print('Connected to :', addr[0], ':', addr[1])

        # Add to our list of clients.
        clients.append(c)

		# Start a new thread and return its identifier 
        start_new_thread(threaded, (c,)) 
    s.close() 


if __name__ == '__main__': 
	Main() 
