import sys
import socket   


def main():
    try:
        host = str(sys.argv[1])
        port = int(sys.argv[2])
        fileName = str(sys.argv[3])
    except:
        print("Error in input")
        exit()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        #sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2048)
        try:
            sock.connect((host,port))
            print("SUCCESS")
        except:
            print("UNSUCCESSFUL")
            exit(1)
        
        command1 = sock.recv(1024)
        print(command1)

        sock.send(b'confirm-accio\r\n')

        command2 = sock.recv(1024)
        print(command2)

        sock.send(b'confirm-accio-again\r\n\r\n')        
        
        command3 = sock.recv(1024)
        print(command3)

main()

   

    





