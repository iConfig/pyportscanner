import argparse  
import sys
import socket


parser = argparse.ArgumentParser()
parser.add_argument('--domain', '-d', type=str , help=" provide domain ")
parser.add_argument('--ports', '-p', nargs='+' ,help='provide ports to scan')
parser.add_argument('--output', '-o', type=str, help="enter a file name to save output into")
args = parser.parse_args()

Domain = args.domain
Ports = args.ports
output_file = args.output

if not Domain:
    print('You must enter a domain name')

try:
    target = socket.gethostbyname(Domain)
    connection =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if Ports:
        for Port in Ports:
            int_port = int(Port) 
            connect = connection.connect_ex((Domain, int_port))
            if connect == 0:
                print(f"port {Port} is open ")
                
                if output_file:
                    with open(output_file,'a') as results:
                        results.write(Port + " is opened " + '\n')
                        results.close()
                else:
                    pass

            else:
                print(f"port {Port} is closed ")
    else:
        number_ports = range(1,65535)
        for number in number_ports:
            int_number = int(number)
            connect_target = connection.connect_ex((Domain, int_number))
            if connect_target == 0:
                print(f"port {number} is opened ")

                if output_file:
                    with open(output_file,'a') as results:
                        results.write(Port + "is opened " + '\n')
                        results.close()
                else:
                    pass
            else:
                # print(f"port {number} is closed ")
                pass
except socket.error:
    print(f"can not connect to {Domain} ")
    connection.close()

except socket.timeout:
    print('connection timeout')
    connection.close()


        
        
