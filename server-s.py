import os
import socket
import sys

def main():
    
    try:
        ipaddress = "0.0.0.0"
        port = int(sys.argv[1])

    
    except:
        sys.stderr.write("ERROR: (Incorect Type [INTS ONLY])")
        exit(1)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            sock.bind((ipaddress,port))
            
            numOfConn = 10
            sock.listen(numOfConn)

            try:
                while True:
                    for x in range(numOfConn):
                        sock.settimeout(10)

                        (clientConnection, clientAddress) = sock.accept()

                        clientConnection.send(b'accio\r\n')

                        recvMsg1 = clientConnection.recv(1024)

                        clientConnection.send(b'accio\r\n')

                        recvMsg2 = clientConnection.recv(1024)                 
                    
                        recvFile = clientConnection.recv(1024)

                        while recvFile:
                            recvFile = clientConnection.recv(1024)
                            
                        length = len(recvFile)
                        print(length)
                                         
            except:
                sys.stderr.write("ERROR: (Could not Listen)\n")
                exit(1)

        except:
            sys.stderr.write("ERROR: (Could not Bind/Execute)\n")
            exit(1)




main()