#!/usr/bin/python3

import socket
import sys
import threading


#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send(b"Welcome to the server. Type something and hit enter\n") #send only takes string

    #infinite loop so that function do not terminate and thread do not end.
    while True:
        print("serving")
        #Receiving from client
        data = conn.recv(1024)
        print(data)
        reply = b'OK...' + data
        if data == b'exit': 
            break

        conn.sendall(reply)

    print("exiting")
    #came out of loop
    conn.close()




HOST = ''   # Symbolic name meaning all available interfaces
PORT = 777 # Arbitrary non-privileged port
server_address = (HOST, PORT)

threads = [] #list of threads


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

#Bind socket to local host and port
try:
    s.bind(server_address)
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print('Socket bind complete')

#Start listening on socket
s.listen(10)
print('Socket now listening')

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))

    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    t=threading.Thread(target=clientthread ,args=(conn,))
    t.start()

s.close()