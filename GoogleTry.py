import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    try:
        print("Trying to Connect")
        sock.connect(('www.google.com', 80))
        print("Connected!")
    except:
        print("Connection Failed")