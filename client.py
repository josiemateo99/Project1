import sys
import socket   

def main():
    try:
        host = str(sys.argv[1])
        port = int(sys.argv[2])
        fileName = str(sys.argv[3])
    except:
        sys.stderr.write("ERROR: (Incorrect Order/Types)")
        exit()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2048)
        try:
            sock.connect((host,port))
            #sock.settimeout(10)
            print("SUCCESS")
        except:
            sys.stderr.write("ERROR: (Incorrect HOST/PORT)")
            exit()
        
        command1 = sock.recv(1024)
        print(command1)

        sock.send(b'confirm-accio\r\n')

        command2 = sock.recv(1024)
        print(command2)

        sock.send(b'confirm-accio-again\r\n\r\n')        
        

        try:
            inputFile = open(fileName, "rb")
        except:
            sys.stderr.write("ERROR: (FILE NOT FOUND)")
            exit()

        fileData = inputFile.read()

        sock.send(fileData)


        print("Sent over")

main()

   

    





