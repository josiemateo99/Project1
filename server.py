#Josephine Mateo-Baez
# PI: 59643111



import threading
import socket
import sys
import os




def connecting(ipaddress, port,directory, counter):
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            sock.bind((ipaddress,port))
            
            sock.listen(1)
            
            try: 
                sock.settimeout(10)
                
                try:

                    while True:
                        
                        

                        (clientConnection, clientAddress) = sock.accept()

                        clientConnection.send(b'accio\r\n')

                        recvMsg1 = clientConnection.recv(1024)

                        clientConnection.send(b'accio\r\n')

                        recvMsg2 = clientConnection.recv(1024)                 
                    
                        #This is where the file gets created and alloted into the file
                        
                        strcounter = str(counter)+ ".file"
                        completeFileName = os.path.join(directory,strcounter) 
                        file = open(completeFileName, 'wb')

                        recvFile = clientConnection.recv(1024)


                        while recvFile:
                            file.write(recvFile)
                            recvFile = clientConnection.recv(1024)
                                            

                        file.close()
                        clientConnection.close()
                        break   

                except:
                    sys.stderr.write("ERROR: (Could not Listen)\n")
                    exit(1)
                    
            except:
                strcounter = str(counter)+ ".file"
                completeFileName = os.path.join(directory,strcounter) 
                file = open(completeFileName, 'w')
                file.write("ERROR")
                file.close()
                clientConnection.close()
                exit(1)
        except:
            sys.stderr.write("ERROR: (Could not Bind/Execute)\n")
            exit(1)
            

            

def main():
    
    try:
        ipaddress = "0.0.0.0"
        port = int(sys.argv[1])
        if port < 1023 or port > 65535:
            sys.stderr.write("ERROR: (Out of Range Port #)\n")
            exit(1)
        directory = sys.argv[2]

    
    except:
        sys.stderr.write("ERROR: (Incorect Type [INTS ONLY])")
        exit(1)

    try:        
        counter = 1

        for _ in range(1,11):
            obj = threading.Thread(target=connecting, args=(ipaddress,port,directory,counter))
            obj.start()
            obj.join()
            counter+= 1
    

    
    except:
        sys.stderr.write("ERROR: (Could not Connect)")
    



main()