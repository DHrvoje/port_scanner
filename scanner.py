import nmap

first = int(input("First port: "))
last = int(input("Last port: "))

target = "127.0.0.1"

scanner = nmap.PortScanner()

for i in range(first, last+1):

    res = scanner.scan(target, str(i))

    res = res['scan'][target]['tcp'][i]['state']

    print(f'port {i} is {res}')