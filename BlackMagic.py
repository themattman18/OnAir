import socket

def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, int(port)))
    s.sendall(content.encode())
    s.shutdown(socket.SHUT_WR)
    while 1:
        data = s.recv(4096)
        if not data:
            break
        print (repr(data))
    print ("Connection Closed")
    s.close()

netcat("192.168.1.187",9993,"play\n")

