import socket  # importing library

ip = socket.gethostbyname(socket.gethostname())  # getting ip-address of host
print(ip)
ip = "52.85.115.59"
# print(ip)
# for port in range(10000):  # check for all available ports
#
#     try:
#
#         serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a new socket
#
#         serv.bind((ip, port))  # bind socket with address
#
#     except:
#
#         print('[OPEN] Port open :', port)  # print open port number
#
#     serv.close()

#conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'toster.ru'
port = 80
t_IP = "mail.ru"
for i in range(50, 500):
    print("ip= ", t_IP, "port= ", i)
    a_socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a_socket.settimeout(1)
    print("s")
    conn = a_socket.connect_ex((t_IP, i))
    if (conn == 0):
        print('Port %d: OPEN' % (i,))
    try:
        service = a_socket.getservbyport(port)
    except Exception:
        service = "unknown"
    print("SERVICE: %-15s\tPORT: %-8d" % (service, port))
    a_socket.close()
print(conn)