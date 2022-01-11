import socket
import os
import re
import subprocess
 

def Start():
    print('[+] Choice')
    print('1 - Scan Network')
    print("2 - Scan Port")
     
    hosts = []
    chemin = os.path.dirname(os.path.abspath(__file__))
    choice = int(input())
    ip = "192.168.43."
    x= 0
    if choice == 1:
        while x<=255:
            p = subprocess.Popen('ping ' +ip+str(x) +" -n 1" ,stdout=subprocess.PIPE, shell=True)
            out, error = p.communicate()
            out = str(out)
            find = re.search("Impossible",out)
            if find is None:
                hosts.append(ip+str(x))
                print("[*] Host found")
                print(ip+str(x))
            x = x + 1
        print("+----------------------+")   
        print("|     hosts:           |")
        print("+----------------------+")
        for host in hosts:
            try:
                name, a ,b =socket.gethostbyaddr(host)
            except name == "Not Found":
                continue
            print('| '+host + " | " + name)
    if choice == 2:
        ip = input("IP a scanner : ")
        try:
            for port in range (1, 1025):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    print("Port : "+ str(port)   +" Ouvert")
                sock.close()
        except socket.gaierror:
            print("serveur non joignable")
        except socket.error:
            print("servveur non joignable")

        print("scan fini")