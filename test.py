import socket
import config as cfg

MY_HOST = socket.gethostname()
MY_IP = socket.gethostbyname(MY_HOST)

udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

print("my udp socket port is " + str(cfg.config["UDP_SOCKET_PORT"]))
print(MY_IP)

print("sending message...")
udp_sock.sendto(str.encode("test message"), ("192.168.2.210", 9500))



