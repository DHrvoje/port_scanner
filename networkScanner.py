from socket import *
import ipaddress
import sys
from flask import Flask
from multiprocessing import Process

app = Flask(__name__)


@app.route("/")
def CheckOpenPortsInAddress(ipAddress):
    print(ipAddress)

    for i in range(0, 1000):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((ipAddress, i))

        if conn == 0:
            print(f'* {i}/tcp open')
        s.close()


@app.route("/")
def CheckOpenPortsInAddressRange(firstIpAddress, lastIpAddress):
    firstIPv4 = ipaddress.IPv4Address(firstIpAddress)
    lastIPv4 = ipaddress.IPv4Address(lastIpAddress)

    for ip_int in range(int(firstIPv4), int(lastIPv4) + 1):
        CheckOpenPortsInAddress(str(ipaddress.IPv4Address(ip_int)))


if __name__ == '__main__':

    server = Process(target=app.run, args=('0.0.0.0', 5000))
    server.start()

    if len(sys.argv) == 3:
        CheckOpenPortsInAddressRange(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        CheckOpenPortsInAddress(sys.argv[1])
    else:
        print(f'Input can have 1 IP address or a range of Ip addresses')

    server.terminate()
    server.join()
