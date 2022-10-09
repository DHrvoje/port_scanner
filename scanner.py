from socket import *
import ipaddress
import sys


def runScanOneArg(ipAddress):
    print(ipAddress)

    for i in range(0, 1000):
        s = socket(AF_INET, SOCK_STREAM)

        s.settimeout(0.001)
        conn = s.connect_ex((ipAddress, i))
        s.settimeout(None)

        if conn == 0:
            print(f'* {i}/tcp open')
        s.close()


def runScanTwoArgs(firstIpAddress, secondIpAddress):
    firstIPv4 = ipaddress.IPv4Address(firstIpAddress)
    secondIPv4 = ipaddress.IPv4Address(secondIpAddress)

    for ip_int in range(int(firstIPv4), int(secondIPv4) + 1):
        runScanOneArg(str(ipaddress.IPv4Address(ip_int)))


if len(sys.argv) == 3:
    runScanTwoArgs(sys.argv[1], sys.argv[2])
else:
    runScanOneArg(sys.argv[1])
