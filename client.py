from fileinput import filename
from pydoc import importfile
import sys
import socket   


def main():
    try:
        host = str(sys.argv[1])
        port = int(sys.argv[2])
        fileName = str(sys.argv[3])
    except:
        print("Error in input")
        exit(1)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((host,port))
            print("SUCCESS")
        except:
            print("UNSUCCESSFUL")
            exit(1)

        try:
            inputFile = open(fileName, "r")
            readFile = inputFile.read()
        except:
            print("File Not Found")
            exit()

        

        



    print(host)
    print(port)

main()

   

    





