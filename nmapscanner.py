#first install nmap Lib by command $ pip3 install python-namp
import nmap

scanner = nmap.PortScanner()
target = input("Enter the target address: ")
scanner.scan(target,"1-1024","-sV")

print("The host name is " + scanner[target].hostname())
print("The host status is " + scanner[target].state())

keys = scanner[target]['tcp'].keys()
for i in keys:
    print('----------------')
    print('the port'+str(i)+':')
    res = scanner[target]['tcp'][i]
    for n in res:
        print(n + ':' + res[n])

        
