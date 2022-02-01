import os
import sys
import socket   

def main():
    try:
        host = str(sys.argv[1])
        port = int(sys.argv[2])
        fileName = str(sys.argv[3])
    except:
        sys.stderr.write("ERROR: (Incorrect Order/Types)")
        exit(1)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2048)
        try: 
            sock.settimeout(10)
            try:
                sock.connect((host,port))
                print("SUCCESS")

                try:
                    command1 = sock.recv(1024)
                    print(command1)

                    sock.send(b'confirm-accio\r\n')

                    command2 = sock.recv(1024)
                    print(command2)

                    sock.send(b'confirm-accio-again\r\n\r\n')        
                    

                    try:
                        inputFile = open(fileName, "rb")
                        
                        file_size = os.path.getsize(fileName)

                        print("Size of File: ", file_size)
                        
                        partialFileData = inputFile.read(1024)

                        while partialFileData:
                            sentFileData = sock.send(partialFileData)
                            partialFileData = inputFile.read(1024)

                    except:
                        sys.stderr.write("ERROR: (FILE NOT FOUND)")
                        exit(1)


                    print("Sent over")

                except:
                    sys.stderr.write("ERROR: UNABLE TO CONNECT TO HOST/PORT")
                    exit(1)
            except:
                sys.stderr.write("ERROR: (TIMED OUT)")
                exit(1)
        except:
            sys.stderr.write("ERROR: (Incorrect HOST/PORT)")
            exit(1)
        

        

main()

   

    





