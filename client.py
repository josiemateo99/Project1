import sys
import socket   

def main():
    try:
        host = str(sys.argv[1])
        port = int(sys.argv[2])
        fileName = str(sys.argv[3])
    except:
        print("ERROR: (Host or Port types incorrect)")
        exit()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2048)
        try:
            sock.connect((host,port))
            print("SUCCESS")
        except:
            print("ERROR: (Unable to Connect)")
            
            exit(1)
        
        command1 = sock.recv(1024)
        print(command1)

        sock.send(b'confirm-accio\r\n')

        command2 = sock.recv(1024)
        print(command2)

        sock.send(b'confirm-accio-again\r\n\r\n')        
        

        try:
            inputFile = open(fileName, "rb")
        except:
            print("File Not Found")
            exit()

        fileData = inputFile.read()

        sock.send(fileData)


        print("Sent over")

main()

   

    





